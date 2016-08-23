from django.forms import ModelForm
from .models import User

class EditForm(ModelForm):
	class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class EditAdminForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name', 'user_level']

class EditPasswordForm(ModelForm):
	class Meta:
        model = User
        fields = ['password', 'password']

class EditDescriptionForm(ModelForm):
	class Meta:
        model = User
        fields = ['description']  
		
		

