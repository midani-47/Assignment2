"""
URL configuration for vanlife_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from blog import views
from django.contrib.auth import views as auth_views
from blog import views as blog_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # path('users/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    path('', blog_views.post_list, name='home'),
    path('', include('blog.urls')), # making the blog myyy home pageeeee
]

