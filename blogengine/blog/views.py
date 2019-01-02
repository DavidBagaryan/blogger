from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'title': 'list posts', 'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', {'title': f'post {slug} detail', 'post': post})
