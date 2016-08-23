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

# Submit registration form
def register(request):
    regstatus = User.userManager.register(**request.POST)
    if regstatus[0]:
        request.session['user_id'] = regstatus[1]
        return redirect(reverse('dashboard:index'))
    else:
        for message in regstatus[1]:
            messages.warning(request, message)
        return redirect(reverse('loginreg:index'))

# Submit login form
def login(request):
    loginstatus = User.usermanager.login(request.POST['email'], request.POST['password'])
    if loginstatus[0]:
        request.session['user_id'] = loginstatus[1]
        return redirect(reverse('books:index'))
    else:
        messages.warning(request, loginstatus[1])
        return redirect(reverse('loginreg:index'))
