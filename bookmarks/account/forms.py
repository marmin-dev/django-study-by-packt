from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    # HTML 에 password 입력으로 취급하도록
    password = forms.CharField(widget=forms.PasswordInput)