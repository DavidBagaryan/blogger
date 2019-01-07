from django.shortcuts import render
from django.views import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'title': 'list posts', 'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


# details
class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagPosts(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_posts.html'


# creates
class CreatePost(ObjectCreateMixin, View):
    model = Post
    form_model = PostForm


class CreateTag(ObjectCreateMixin, View):
    model = Tag
    form_model = TagForm


# updaters
class UpdatePost(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm


class UpdateTag(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm


# deletes
class DeletePost(ObjectDeleteMixin, View):
    model = Post


class DeleteTag(ObjectDeleteMixin, View):
    model = Tag
