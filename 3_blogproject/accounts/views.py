from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.conf import settings

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(
#             request, username=username, password=password
#         )
#
#         if user is not None:
#             auth.login(request, user)
#
#             return redirect('home')
#
#         else:
#             return render(request, "login.html", {
#                 'error': 'Username or Password is incorrect.',
#             })
#
#     else:
#         return render(request, "login.html")

class Loginviews(LoginView):
    template_name = 'login.html'

login = Loginviews.as_view()

# @login_required
# def logout(request):
#     if request.method == "POST":
#         auth.logout(request)
#
#     return redirect("home")

class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL

logout = LogoutViews.as_view()

# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username=request.POST['username'],
#                 password=request.POST['password1']
#             )
#             auth.login(request, user)
#
#             return redirect('home')
#
#     return render(request, "signup.html")

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
