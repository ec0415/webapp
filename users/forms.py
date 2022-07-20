from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#inherits django UserCreationForm and makes additions/changes -- add email field
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


#update username and email (this is a model form -- a form that works with a specific data base model)
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


#update profile pic (this is a model form -- a form that works with a specific data base model)
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']