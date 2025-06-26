from django.contrib.sitemaps import Sitemap

from blog.models import Post


# sitemaps 모듈의 Sitemap 클래스 상속으로 커스텀 사이트맵 정의

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    # 이 사이트맵에 포함할 객체들의 QuerySet을 반환
    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.updated