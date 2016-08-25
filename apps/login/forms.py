from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }))
    password = forms.CharField(max_length=45, widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder': 'Password'
        }))

class RegisterForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=45, widget=forms.PasswordInput)
