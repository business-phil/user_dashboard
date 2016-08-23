from django.shortcuts import render, redirect
from .models import User
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Login and reg at homepage
def index(request):
    request.session.clear()
    # loginform = AuthenticationForm
    # regform = UserCreationForm
    context = {
        # "login":loginform,
        # "reg":regform,
    }
    return render(request, 'login/index.html', context)

# Submit login form
def login(request):  #POST
    pass

# Submit registration form
def register(request):  #POST
    pass
