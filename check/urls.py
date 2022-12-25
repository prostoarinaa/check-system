from django.urls import path
from . import views


app_name = 'check'
urlpatterns = [
    path('', views.home, name='home'),
    path(r'login/', views.UserLoginView.as_view(), name='login'),
    path(r'register/', views.register, name='register'),
    path(r'logout/', views.logout_user, name='logout'),

    path(r'add_lesson/', views.add_lesson, name='add_lesson'),
    path(r'add_mark/', views.add_mark, name='add_mark'),
    path(r'show_marks/', views.show_marks, name='show_marks'),
]