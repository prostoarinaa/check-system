from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Lesson, User, Mark
from datetime import date

from .forms import LoginForm, UserRegistrationForm, AddLessonForm, AddMarkForm


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


def add_lesson(request):
    if request.method == 'GET':
        form = AddLessonForm()
        return render(request, 'add_lesson.html', {'form': form})

    if request.method == 'POST':
        form = AddLessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            return redirect('check:home')
        else:
            return render(request, 'add_lesson.html', {'form': form})


def add_mark(request):
    form = AddMarkForm()

    if request.method == 'GET':
        # student = request.user.username
        return render(request, 'add_mark.html', {'form': form})

    if request.method == 'POST':
        form = AddMarkForm(request.POST)
        if form.is_valid():
            print(form.fields)
            mark = form.save(commit=False)
            mark.student = request.user
            mark.save()
            # lessons = Lesson.objects.filter(date=date.today())
            return redirect('check:home')

    return render(request, 'add_mark.html', {'form': form})
    # if request.method == 'POST':
    #     form = AddMarkForm(request.POST)
    #     if form.is_valid():
    #         mark = form.save(commit=False)
    #         mark.save()
    #         return redirect('check:home')
    #     else:
    #         return render(request, 'add_mark.html', {'form': form})


# @login_required
def home(request):
    return render(request, 'home.html')


def show_marks(request):
    marks = Mark.objects.all()
    return render(request, 'show_marks.html', {'marks': marks})
