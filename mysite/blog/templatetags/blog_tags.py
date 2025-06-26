from django import template
from django.utils.safestring import mark_safe

from blog.models import Post
from django.db.models import Count

import markdown

register = template.Library()

# 게시물 개수 보여주는 커스텀 태그
@register.simple_tag
def total_posts():
    return Post.objects.count()

# 최근 게시물 5개 보여주는 커스텀 태그
@register.inclusion_tag('blog/post/latest_posts.html')
# 인클루전 태그를 사용하면 템플릿 태그에서 반환된 콘텍스트 변수로 템플릿을 렌더링 할 수 있다.
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# 댓글 많은 순 리스트 보여주는 커스텀 태그
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]


# 게시물에서 마크다운 구문 사용 게시물 본문 HTML 로 변환 가능 커스텀 필터
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))