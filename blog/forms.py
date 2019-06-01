from django import forms
from .models import Comments, Post

class commentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields =('author', 'body')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body')

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
		