from django.urls import path
from . import views


urlpatterns =[
    path('', views.post_list, name='post_list'),
    # path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike/', views.post_unlike, name='post_unlike'),
    path('journeys/', views.journey_list, name='journey_list'),
    path('journey/new/', views.journey_new, name='journey_new'),
    path('journey/<int:pk>/', views.journey_detail, name='journey_detail'),
    path('journey/<int:pk>/join/', views.journey_join, name='journey_join'),
    path('journey/<int:pk>/leave/', views.journey_leave, name='journey_leave'),
    path('feed/', views.blog_feed, name='blog_feed'),
]
