from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class LoginForm(AuthenticationForm):
    pass


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'fullname', 'password1']

