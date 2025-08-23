from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from shop.sitemap import ProductSitemap
from blog.sitemap import BlogSitemap

sitemaps = {
    'products': ProductSitemap,
    'blog': BlogSitemap,
}

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
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
