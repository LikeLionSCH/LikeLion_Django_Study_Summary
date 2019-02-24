from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('delete/<int:blog_id>/', views.delete, name="delete"),
    path('edit/<int:blog_id>/', views.edit, name="edit"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('search/', views.search, name="search"),
]
