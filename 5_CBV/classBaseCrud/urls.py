from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogView.as_view(), name="list"),
    path("create/", views.BlogCreate.as_view(), name="create"),
    path("read/<int:pk>", views.BlogRead.as_view(), name="read"),
    path("update/<int:pk>", views.BlogUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.BlogDelete.as_view(), name="delete"),
]
