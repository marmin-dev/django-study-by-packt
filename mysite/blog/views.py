import os

from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from dotenv import load_dotenv
from taggit.models import Tag

import blog
from .forms import EmailPostForm, CommentForm
from .models import Post

# 변수 불러오기
load_dotenv()

# 포스트 목록
def post_list(request, tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # page_number 이 정수가 아닌 경우 첫 번째 페이지 전달
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts, 'tag':tag})


# # 포스트 목록 클래스
# class PostListView(ListView):
#     queryset = Post.objects.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


# 포스트 상세 페이지
# 이 글의 active 댓글 목록
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # 이 글의 active 댓글 목록
    comments = post.comments.filter(active=True)
    # 사용자가 댓글을 달 수 있는 폼
    form = CommentForm()
    # 유사한 게시물들의 목록
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html',
                  {'post':post,
                   'comments':comments,
                   'form':form,
                   'similar_posts':similar_posts})


# 포스트 공유
def post_share(request, post_id):
    # id로 게시물 조회
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        # 폼이 제출되었다면
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url} \n\n"
            send_mail(subject, message, os.getenv("EMAIL_USER"), [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',
                  {'post': post, 'form': form, 'sent':sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # 댓글이 달림
    form = CommentForm(data = request.POST)
    if form.is_valid():
        # 데이터 베이스에 저장하지 않고 Comment 객체 만들기
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html',
                  {'post':post, 'form': form, 'comment':comment})



