from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .forms import LoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


def logout_user(request):
    logout(request)
    return redirect('check:home')


def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('check:home')
        else:
            return render(request, 'register.html', {'form': form})


# @login_required
def home(request):
    return render(request, 'home.html')

