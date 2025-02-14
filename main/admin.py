from django.contrib import admin
from .models import Contact,Category,News,NewsImage,Comments,Like,Projects,Employees
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = "Kategoriya nomi yoki qisqartmasi."
    list_per_page = 100


class NewsImageAdmin(admin.TabularInline):
    model = NewsImage
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    image_preview.short_description = "Rasm"


@admin.action(description='Yangiliklarni faol qilish')
def make_active(self, request, queryset):
    queryset.update(is_active=True)

@admin.action(description='Yangiliklarni faol emas qilish')
def make_inactive(self, request, queryset):
    queryset.update(is_active=False)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creator', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    list_per_page = 100
    save_on_top = True
    prepopulated_fields = {
        'slug': ('title',)
    }
    inlines = [NewsImageAdmin]
    actions = [make_active, make_inactive]  # Yangiliklarni faol qilish va faol emas qilish uchun amalga oshirish uchun actions qo'shishimiz mumkin.

    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email')
    search_help_text = "Ism, familiya, email yoki telefon bo‘yicha qidiring."
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 100
    save_on_top = True
    actions = ["export_to_csv"]

    # Maxsus action: CSV eksport qilish
    def export_to_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="callback_requests.csv"'
        writer = csv.writer(response)
        writer.writerow(["Ism", "Familya", "Elektron pochta", "Telefon raqam", "Xabar", "Yaratilgan vaqti"])
        for obj in queryset:
            writer.writerow([obj.first_name, obj.last_name, obj.email, obj.phone_number, obj.message, obj.created_at])
        return response

    export_to_csv.short_description = "CSV formatda eksport qilish"



@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('news', 'name', 'comment', 'created_at')
    list_filter = ('news', 'created_at')
    search_fields = ('name', 'comment')
    search_help_text = "Foydalanuvchi nomi yoki sharh matni bo'yicha qidirish"
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 50
    save_on_top = True

    # Adding actions
    actions = ["delete_selected_comments"]

    def delete_selected_comments(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} ta sharh o'chirildi.")
    delete_selected_comments.short_description = "Tanlangan sharhlarni o'chirish"


# Like modelini admin panelga qo'shish
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('news', 'count', 'get_news_category', 'get_news_creator', 'get_news_created_at')  # Ko'rinadigan ustunlar
    list_filter = ('news__category',)  # Kategoriya bo'yicha filtr
    search_fields = ('news__title',)  # Yangilik sarlavhasi bo'yicha qidirish
    ordering = ('-count',)  # Like soniga qarab tartiblash
    list_per_page = 20  # Har bir sahifada ko'rsatiladigan yozuvlar soni

    # Yangilik kategoriyasini ko'rsatish uchun custom method
    def get_news_category(self, obj):
        return obj.news.category.name
    get_news_category.short_description = 'Kategoriya'

    # Yangilik yaratuvchisini ko'rsatish uchun custom method
    def get_news_creator(self, obj):
        return obj.news.creator
    get_news_creator.short_description = 'Yaratuvchi'

    # Yangilik yaratilgan vaqtni ko'rsatish uchun custom method
    def get_news_created_at(self, obj):
        return obj.news.created_at
    get_news_created_at.short_description = 'Yaratilgan vaqt'
    get_news_created_at.admin_order_field = 'news__created_at'




@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'events', 'created_at']
    list_filter = ('created_at', 'events')
    search_fields = ('title', 'events', 'created_at')
    date_hierarchy = 'created_at'
    list_per_page = 100
    
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'created_at']
    list_filter = ('position', 'created_at')
    search_fields = ('first_name', 'last_name', 'position')
    date_hierarchy = 'created_at'
    list_per_page = 100
    actions = ["export_to_csv"]

    # Maxsus action: CSV eksport qilish
    def export_to_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'
        writer = csv.writer(response)
        writer.writerow(["Ism", "Familya", "Lavozimi", "Yaratilgan vaqti"])
        for obj in queryset:
            writer.writerow([obj.first_name, obj.last_name, obj.position, obj.created_at])
        return response