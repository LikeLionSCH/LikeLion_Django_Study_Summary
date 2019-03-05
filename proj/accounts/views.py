from django.shortcuts import render
from .models import Pictures

# Create your views here.

def index(request):
    pictures = Pictures.objects

    return render(request, 'index.html', {
        "pictures": pictures,
    })
