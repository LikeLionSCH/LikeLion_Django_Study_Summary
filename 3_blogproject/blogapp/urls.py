from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('<int:blog_id>/delete/', views.delete, name="delete"),
    path('<int:blog_id>/edit/', views.edit, name="edit"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('search/', views.search, name="search"),
]
