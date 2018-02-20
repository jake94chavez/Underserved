from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.save()
		return user
