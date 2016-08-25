from django import forms
from .models import User
from ..login.forms import RegisterForm

class EditForm(forms.Form):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=45)
	last_name = forms.CharField(max_length=45)

	def __init__(self, **kwargs):
		user = kwargs.pop('user', None)
		super(EditForm, self).__init__()
		if user:
			self.fields['email'].initial = user.email
			self.fields['first_name'].initial = user.first_name
			self.fields['last_name'].initial = user.last_name

class EditAdminForm(forms.Form):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=45)
	last_name = forms.CharField(max_length=45)
	user_level = forms.ChoiceField([('admin', 'admin'), ('user', 'user')])

	def __init__(self, **kwargs):
		user = kwargs.pop('user', None)
		super(EditAdminForm, self).__init__()
		if user:
			self.fields['email'].initial = user.email
			self.fields['first_name'].initial = user.first_name
			self.fields['last_name'].initial = user.last_name
			self.fields['user_level'].initial = user.user_level

class EditPasswordForm(forms.Form):
	password = forms.CharField(max_length=45, widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=45, widget=forms.PasswordInput)

class EditDescriptionForm(forms.Form):
	description = forms.CharField(max_length=255, widget=forms.Textarea, label='')

	def __init__(self, **kwargs):
		user = kwargs.pop('user', None)
		super(EditDescriptionForm, self).__init__()
		if user:
			self.fields['description'].initial = user.description
