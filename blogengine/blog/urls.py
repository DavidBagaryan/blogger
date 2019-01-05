from django.urls import path

from .views import posts_list, tags_list, ObjectCreatePost, ObjectCreateTag, PostDetail, TagPosts

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post/create/', ObjectCreatePost.as_view(), name='create_post'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/create/', ObjectCreateTag.as_view(), name='create_tag'),
    path('tag/<str:slug>/', TagPosts.as_view(), name='tag_posts'),
]