from django.contrib import admin
from blog.models import Post, Comment


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'created'] # 리스트에 보여질 목록
    list_filter = ['author', 'publish', 'created', 'author'] # 속성에 포함된 필드별로 결과 필터링
    search_fields = ['title', 'body'] # 검색 조건
    prepopulated_fields = {'slug': ('title',)} # 타
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'body', 'created', 'active']
    list_filter = ['active', 'created', 'email', 'body']
    search_fields = ['name', 'email', 'body']