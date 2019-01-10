from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('author/<name>', views.getauthor, name='author'),
    path('article/<int:id>', views.getsingle, name='single_post')

]
