from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ClassBlog


class BlogView(ListView):
    model = ClassBlog


class BlogCreate(CreateView):
    model = ClassBlog
    fields = ["title", "body"]
    success_url = reverse_lazy('list')


class BlogRead(DetailView):
    model = ClassBlog
    

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ["title", "body"]
    success_url = reverse_lazy("list")


class BlogDelete(DeleteView):
    mdoel = ClassBlog
    success_url = reverse_lazy("list")
