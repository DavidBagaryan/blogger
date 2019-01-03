from django.shortcuts import render, redirect
from django.views import View

from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm


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


class CreateTag(View):
    def get(self, request):
        return render(request, 'blog/create_tag.html', context={'form': TagForm()})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(request, 'blog/create_tag.html', context={'form': bound_form})
