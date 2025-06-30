from django.urls import path

from account import admin, views

urlpatterns = [
    path('login/', views.user_login, name='login'),
]