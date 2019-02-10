from django.shortcuts import render
from .models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects

    return render(request, "portfolio.html", {
        "portfolios": portfolios,
    })
