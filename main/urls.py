from django.urls import path
from .views import HomeView,ServiceView,AboutView,TermsandConditionsView,BlogView,ContactView,NewsDetailView
from .views import custom_404_view
from django.conf.urls import handler404

handler404 = custom_404_view  # 404 errorni o'qish uchun custom view qo'yish

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('service/', ServiceView, name='service'),
    path('terms-and-conditions/', TermsandConditionsView, name='termsandconditions'),
    path('blog/', BlogView, name='blog'),
    path('news/<str:slug>/', NewsDetailView, name='newsdetail'),
    path('contact/', ContactView, name='contact'),
]