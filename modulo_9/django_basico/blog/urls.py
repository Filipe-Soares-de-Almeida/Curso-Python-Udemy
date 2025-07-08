from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
  path('<int:post_id>/', views.post, name='post'),
  path('', views.blog, name='home'),
  path('exemplo/', views.exemplo, name='exemplo'),
]