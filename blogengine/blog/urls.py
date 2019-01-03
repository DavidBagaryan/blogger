from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>/', TagPosts.as_view(), name='tag_posts'),
]