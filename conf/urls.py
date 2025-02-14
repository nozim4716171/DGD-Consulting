from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),    # main app'ning urls.py ga yo'naltiramiz
)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media faqat debug rejimida yo'q
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # static faqat debug rejimida yo'q
