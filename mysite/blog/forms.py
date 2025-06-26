from django import forms
from .models import  Comment

# 이메일 폼
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea)

# 동적으로 만들기 위해 모델 폼 사용
# 댓글 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

# 게시글 검색 폼
class SearchForm(forms.Form):
    query = forms.CharField()