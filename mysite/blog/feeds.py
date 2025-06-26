import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy

from blog.models import Post

# 피드 보여주기
# 신디케이션 프레임워크의 Feed 클래스를 상속받아 피드를 정의
class LatestPostsFeed(Feed):
    title = 'myblog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog'

    # 5개 아이템 반환
    def items(self):
        return Post.published.all()[:5]

    # 포스트 제목 반환
    def item_title(self, item):
        return item.title

    # 포스트 내용 반환
    def item_description(self, item):
        return truncatewords(markdown.markdown(item.body), 30)

    # 포스트 등록일 반환
    def item_pubdate(self, item):
        return item.publish