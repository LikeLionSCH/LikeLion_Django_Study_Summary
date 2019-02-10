from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog


def home(request):
    blogs = Blog.objects

    return render(request, "home.html", {
        "blogs": blogs,
    })


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)

    return render(request, "detail.html", {
        "details": details,
    })


def new(request):
    return render(request, "new.html")


def create(request):
    blog = Blog()

    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()

    blog.save()

    return redirect('/blog/' + str(blog.id))


def search(request):
    post_list = Blog.objects.all()
    keyword = request.GET.get('keyword', '')

    if keyword:
        post_list = post_list.filter(title__icontains=keyword)

    return render(request, "search.html", {
        'post_list': post_list,
        'keyword': keyword
    })
