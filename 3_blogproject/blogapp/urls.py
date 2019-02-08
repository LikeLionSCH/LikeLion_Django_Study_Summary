from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name="search"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]
