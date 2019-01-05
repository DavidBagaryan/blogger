from django.shortcuts import render  # , redirect
from django.views import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'title': 'list posts', 'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagPosts(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_posts.html'


class ObjectCreateTag(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/create_tag.html'


class ObjectCreatePost(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/create_post.html'
