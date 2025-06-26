from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog.sitemaps import PostSitemap

sitemaps = {
    'posts' : PostSitemap
}
urlpatterns = [
    # 관리자
    path('admin/', admin.site.urls),
    # 블로그 애플리케이션
    path('blog/',include('blog.urls', namespace='blog')),
    # 사이트 맵
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
