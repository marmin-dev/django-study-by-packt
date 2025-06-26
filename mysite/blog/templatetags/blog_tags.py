from django import template
from blog.models import Post
from django.db.models import Count

register = template.Library()

# 게시물 개수 보여주는 커스텀 태그
@register.simple_tag
def total_posts():
    return Post.objects.count()

# 최근 게시물 5개 보여주는 커스텀 태그
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# 댓글 많은 순 리스트 보여주는 커스텀 태그
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]