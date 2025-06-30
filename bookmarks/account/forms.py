from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    # HTML 에 password 입력으로 취급하도록
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password",widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']