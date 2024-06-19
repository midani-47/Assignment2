from django.urls import path
from . import views
from django.urls import path, include
from .views import home, register, login, logout


urlpatterns= [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/blogs/', views.profile_blogs, name='profile_blogs'),
    path('liked-blogs/', views.liked_blogs, name='liked_blogs'),
    path('search/', views.search, name='search'),

    # path('profile/<str:username>/follow/', views.follow_unfollow_user, name='follow_unfollow_user'),
]