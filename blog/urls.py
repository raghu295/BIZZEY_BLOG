from django.urls import path
from blog.views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', log_in, name="login"),
    path('register', register, name="register"),
    path('blog', blog, name="blog"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('create-blog', create_blog, name="add_your_blog"),
    path('blog-detail/<int:blog_id>', blog_detail, name="blog_detail_page"),
    path('logout', log_out, name="user_logout"),
    path('blog-remove/<int:blog_id>', blog_delete, name="blog_delete_page"),
    path('blog-update/<int:blog_id>', blog_update, name="blog_update_page"),
    path('profile', profile_page, name="profile_page"),
]
