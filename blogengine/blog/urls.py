from django.urls import path

from .views import posts_list, tags_list, CreatePost, CreateTag, PostDetail, TagPosts, UpdateTag, UpdatePost, \
    DeletePost, DeleteTag

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('posts/', posts_list, name='posts_list'),
    path('post/create/', CreatePost.as_view(), name='create_post'),
    path('post/<str:slug>/update/', UpdatePost.as_view(), name='update_post'),
    path('post/<str:slug>/delete/', DeletePost.as_view(), name='delete_post'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),

    path('tags/', tags_list, name='tags_list'),
    path('tag/create/', CreateTag.as_view(), name='create_tag'),
    path('tag/<str:slug>/update/', UpdateTag.as_view(), name='update_tag'),
    path('tag/<str:slug>/delete/', DeleteTag.as_view(), name='delete_tag'),
    path('tag/<str:slug>/', TagPosts.as_view(), name='tag_posts'),
]