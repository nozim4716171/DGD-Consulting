from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]



class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name=_("Slug"))
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Creator"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name=_("Video"))


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-created_at"]


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_("News"))
    image = models.ImageField(upload_to="news_images/", verbose_name=_("Image"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.news.title} - {self.created_at.strftime('%d %b %Y')}"
    
    class Meta:
        verbose_name = "News Image"
        verbose_name_plural = "News Images"




class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("First name"))
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Last name"))
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Phone number"))
    email = models.EmailField(max_length=255, verbose_name=_("Email address"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_("News"))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Name"))
    comment = models.TextField(blank=True,null=True, verbose_name=_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d %b %Y')}"
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_("News"))
    count = models.PositiveIntegerField(default=0, verbose_name=_("Count"))
    
    def __str__(self):
        return f"{self.news.title} - {self.count}"
    
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"



class Projects(models.Model):
    EVENTS = (
        ('ekspeditsiya', _('Ekspeditsiya')),
        ('konferensiyalar', _('konferensiya')),
        ('amaliy seminar', _('Amaliy seminar')),
        ('geologik sayohatlar', _('Geologik sayohatlar')),
        ('vebinarlar', _('Vebinarlar')),
        ('kashfiyotlar', _('Kashfiyotlar')),
        ('treninglar', _('Treninglar')),
        ('forumlar', _('Forumlar')),
        ('ilmiy taqdimotlar', _('Ilmiy taqdimotlar'))
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    events = models.CharField(max_length=100, choices=EVENTS, verbose_name=_("Events"))
    created_at = models.DateField(verbose_name=_('Created At'))
    image = models.ImageField(upload_to="projects/images/", default='rasm.png', verbose_name=_("Image"))


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Employees(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("First name"))
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Last name"))
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Position"))
    image = models.ImageField(upload_to="employees/images/", default='rasm.png', verbose_name=_("Image"))
    instagram_url = models.URLField(default='https://instagram.com/', blank=True, null=True, verbose_name=_("Instagram link URL"))
    facebook_url = models.URLField(default='https://facebook.com/', blank=True, null=True, verbose_name=_("Facebook link URL"))
    telegram_url = models.URLField(default='https://t.me/', blank=True, null=True, verbose_name=_("Telegram link URL"))
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["-created_at"]

