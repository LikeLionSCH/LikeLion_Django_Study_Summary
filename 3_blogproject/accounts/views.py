from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.conf import settings


class Loginviews(LoginView):
    template_name = 'login.html'


login = Loginviews.as_view()


class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL


logout = LogoutViews.as_view()


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(settings.LOGIN_URL)

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form,
    })
