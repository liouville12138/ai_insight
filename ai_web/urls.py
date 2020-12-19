from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
   path('', views.index, name='ai_web'),
   path('image_recognition/', views.image_recognition, name='image_recognition'),
   path('upload_file/', views.upload_file, name='upload_file'),
]