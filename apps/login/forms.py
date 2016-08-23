from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)
    conf_password = forms.CharField(max_length=45, widget=forms.PasswordInput)
