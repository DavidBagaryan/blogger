from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render
from django.views import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm


def posts_list(request):
    context = check_for_user_search(request, Post).copy()
    paginator = {'page_obj': get_paginated_list(request, context['list'])}
    context.update(paginator)

    return render(request, 'blog/index.html', context=context)


def tags_list(request):
    context = check_for_user_search(request, Tag).copy()
    return render(request, 'blog/tags_list.html', context=context)


def check_for_user_search(request, model):
    search = request.GET.get('user_search', None)
    found = None

    if search:
        if model is Post:
            output = model.objects.filter(models.Q(title__icontains=search) | models.Q(body__icontains=search))
        else:
            output = model.objects.filter(models.Q(title__icontains=search))

        found = output.count
    else:
        output = model.objects.all()

    return {'found': found, 'list': output}


def get_paginated_list(request, list_objects):
    per_page = 2
    default_page_num = 1
    paginator = Paginator(list_objects, per_page=per_page)
    return paginator.get_page(request.GET.get('page', default_page_num))


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
