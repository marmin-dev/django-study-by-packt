from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from account.models import Profile
from account.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm



# 로그인
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request=request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authentication successfully")
                else:
                    return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html',{'form':form})


# 회원 가입
def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # 유저 객체를 생성하지만 실제 저장은 하지 않음
            new_user = user_form.save(commit=False)
            # 새로운 패스워드 선택
            new_user.set_password(user_form.cleaned_data['password'])
            # 오브젝트 저장
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'account/register.html',
        {'user_form':user_form}
    )


# 대시보드
@login_required
def dashboard(request):
    return render(request,
                  "account/dashboard.html",
                  {'section':'dashboard'})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        'account/edit.html',
        {
            "user_form":user_form,
            "profile_form":profile_form
        }
    )


