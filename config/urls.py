from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/' , include('ckeditor_uploader.urls')),
    path('' , include('home.urls')),
    path('account/' , include('account.urls')),
    path('blog/' , include('blog.urls')),
    path('shop/' , include('shop.urls')),
    path('about_us/' , include('about_us.urls')),
    path('contactus/' , include('contactus.urls')),
    path('cart/' , include('cart.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
