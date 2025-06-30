from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # 로그인
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # 로그아웃
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 대시보드
    path('', views.dashboard, name='dashboard'),
]