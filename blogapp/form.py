from django import forms
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = [
			'title',
			'body',
			'image',
			'category'
		]

class RegisterUser(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'email',
			'username',
			'password1',
			'password2'
		]
		