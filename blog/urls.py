from django.urls import path
from .views import (
    test,
    BlogListView,
    UserBlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    RegisterView,
    )

from django.contrib.auth import views as auth_views

## for logout view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    ## for testing 
    path('test/',test, name= "test"),

    ## authentication url
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page ='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    ## web routes
    path('', BlogListView.as_view(), name='home'),
    path('user_blogs/', UserBlogListView.as_view(), name='user_blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    
]