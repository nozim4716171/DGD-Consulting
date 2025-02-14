from django.shortcuts import render,redirect
from .forms import ContactForm,CommentsForm
from django.contrib import messages
from django.http import JsonResponse
import asyncio
from aiogram import Bot
from django.conf import settings
from .models import News,Comments,Like,Projects,Employees
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

# Create your views here.
def HomeView(request):
    projects = Projects.objects.all().order_by('-created_at')[:4]
    context = {
        'projects': projects,
    }
    return render(request, 'home.html' ,context)


def ServiceView(request):
    return render(request,'service.html')

def AboutView(request):
    employees = Employees.objects.all().order_by('-created_at')[0:5]
    context = {
        'employees': employees,
    }
    return render(request, 'about.html', context)

def TermsandConditionsView(request):
    return render(request, 'termscond.html')



def BlogView(request):
    news_list = News.objects.filter(is_active=True).order_by('-created_at')[0:3] 
    news_list2 = News.objects.filter(is_active=True).order_by('-created_at')[3:7]
    
    context = {
        'news_list': news_list,
        'news_list2': news_list2,  
    }
    return render(request, 'blog.html', context=context)

def NewsDetailView(request, slug):
    # Yangilikni slug orqali olish
    news = get_object_or_404(News, slug=slug)

    # O'xshash yangiliklarni olish (kategoriyaga ko'ra)
    similar_news = News.objects.filter(category=news.category).order_by('-created_at')[:4]

    # Ushbu yangilikka oid barcha izohlarni olish
    comments = Comments.objects.filter(news=news).order_by('-created_at')

    # Ushbu yangilikning yoki barcha izohlarni soni
    comment_count = len(comments)

    # Eng so'nggi 4 ta yangilikni olish 
    last_news = News.objects.all().order_by('-created_at')[:4]

     # Like ma'lumotlarini olish yoki yaratish
    like, created = Like.objects.get_or_create(news=news)

    # Sessiyadan foydalanuvchi "like" qilganligini tekshirish
    liked_news = request.session.get('liked_news', [])
    user_liked = news.id in liked_news

    # Agar "like_button" GET parametr orqali kelgan bo'lsa
    if 'like_button' in request.GET:
        if not user_liked:
            like.count += 1
            like.save()
            liked_news.append(news.id)  # Yangilik ID sini sessiyaga qo'shish
            request.session['liked_news'] = liked_news
            request.session.modified = True
            messages.success(request, "Yangilik yoqtirildi!")
        else:
            messages.error(request, _("Siz ushbu yangilikni allaqachon yoqtirgansiz."))
        return redirect('newsdetail', slug=slug)

    # Izoh formasi yuborilishini boshqarish
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news  # Hozirgi yangilikni sharh bilan bog'lash
            comment.save()
            messages.success(request, _("Sharhingiz muvaffaqiyatli yuborildi!"))
            return redirect('newsdetail', slug=slug)
        else:
            messages.error(request, _("Sharh yuborishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring."))
    else:
        form = CommentsForm()


    context = {
        'news': news,
        'similar_news': similar_news,
        'form': form,
        'comments': comments,
        'comment_count': comment_count,
        'last_news': last_news,
        'like_count': like.count,
        'user_liked': user_liked,  # Foydalanuvchi "like" qilganligini konteksga uzatish
    }
    return render(request, 'news-detail.html', context)

async def send_telegram_message(data):
    """
    Telegram orqali xabar yuboradi
    """
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    message = (
        "📩 Yangi kontakt form so'rovi:\n\n"
        f"👤 Ism: <b>{data['first_name']}</b>\n"
        f"👤 Familya: <b>{data['last_name']}</b>\n"
        f"📧 Email: <b>{data['email']}</b>\n"
        f"📞 Telefon: <b>{data['phone_number']}</b>\n"
        f"📝 Xabar: <b>{data['message']}</b>\n"
    )
    await bot.send_message(chat_id=settings.TELEGRAM_ADMIN_ID, text=message, parse_mode='HTML')
    await bot.close()

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data     # So'rovlarni olish uchun

            form.save()  # Ma'lumotlarni saqlash

            # Telegramga xabar yuborish
            asyncio.run(send_telegram_message(form_data))

            return JsonResponse({"success": True, "message": _("Sizning so'rovingiz qabul qilindi!")})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "message": _("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring."), "errors": errors}, status=400)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)