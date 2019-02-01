from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects

    return render(request, "home.html",
                  {"blogs": blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)

    return render(request, "detail.html",
                  {"details": details})
