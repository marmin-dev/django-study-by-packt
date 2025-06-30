from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # 로그인
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # 로그아웃  - POST 메서드만 동작한다.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 대시보드
    path('', views.dashboard, name='dashboard'),
    # 비밀 번호 변경
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    # 비밀 번호 변경 완료
    path(
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    )
]