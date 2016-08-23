from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm

# Login and reg at homepage
def index(request):
    request.session.clear()
    context = {
        'regform': RegisterForm,
        'loginform': LoginForm
    }
    return render(request, 'login/index.html', context)

# Submit login form
def login(request):  #POST
    pass

# Submit registration form
def register(request):  #POST
    # regstatus = User.userManager.register(**request.POST)
    pass
