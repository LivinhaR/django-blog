from django.urls import path
from blog.views import (index, ola, get_all_posts, get_post, PostCreateView, create_post, PostListView, SobreTemplateView)

urlpatterns = [
    path('index/', index, name= "index"),
    path('ola/', ola, name= "ola"),
    path('api/posts', get_all_posts, name="posts_data"),
    path('api/posts/<int:post_id>', get_post, name="post_data"),
    path('post/add', PostCreateView.as_view(), name="post_add"),
    path('api/post/add', create_post, name="create_post_data"),
    path('posts', PostListView.as_view(), name="posts_all"),
    path('about-us', SobreTemplateView.as_view(), name="about_page"),
]
