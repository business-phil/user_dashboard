from django import forms
from .models import User
from ..login.forms import RegisterForm

class EditForm(forms.Form):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=45)
	last_name = forms.CharField(max_length=45)

class EditAdminForm(forms.Form):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=45)
	last_name = forms.CharField(max_length=45)
	user_level = forms.CharField(max_length=45)


class EditPasswordForm(forms.Form):
	password = forms.CharField(max_length=45, widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=45, widget=forms.PasswordInput)


class EditDescriptionForm(forms.Form):
	description = forms.CharField(max_length=255)
