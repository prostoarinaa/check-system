from django.urls import path
from . import views


app_name = 'check'
urlpatterns = [
    path('', views.home, name='home'),
    path(r'login/', views.UserLoginView.as_view(), name='login'),
    path(r'register/', views.register, name='register'),
    path(r'logout/', views.logout_user, name='logout'),

]