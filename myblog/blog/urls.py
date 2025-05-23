from django.urls import path
from .views import blog_list, blog_detail, create_blog_post

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('new/', create_blog_post, name='create_blog_post'),
    path('<int:post_id>/', blog_detail, name='blog_detail'),  # Detail page
]