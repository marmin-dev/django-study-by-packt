from django.http import Http404
from django.shortcuts import render, get_object_or_404

import blog
from .models import Post


# 포스트 목록
def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})


# 포스트 상세 페이지
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post':post})
