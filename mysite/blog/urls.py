from django.urls import path

from blog import views
from blog.feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    # post 뷰
    path('', views.post_list, name='post_list'),
    # 태그명으로 게시물
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    # 상세 페이지 - SEO 상 이점을 살리기 위해 라우팅 조건 설정
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    # 이메일로 게시물 공유하기
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    # 포스트에 댓글 추가
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    # 포스트 피드
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]