from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Message, Comment
from .forms import RegisterForm, EditForm, EditAdminForm, EditPasswordForm, EditDescriptionForm

# user/admin home page
def index(request):
    if not 'user_id' in request.session:
        return redirect(reverse('login:index'))
    current_user = User.objects.get(id=request.session['user_id'])
    user = User.objects.all()
    context = { 'users': user }
    if current_user.user_level == 'admin':
        return render(request, 'dashboard/index_admin.html', context)
    else:
        return render(request, 'dashboard/index.html', context)

# edit page for users and admin
def edit(request, user_id):
    if not 'user_id' in request.session:
        return redirect(reverse('login:index'))
    user = User.objects.get(id=request.session['user_id'])
    # redirect user accessing other user pages
    if user.id != int(user_id) and user.user_level == 'user':
        return redirect(reverse('dashboard:edit', args=[user.id]))
    urlUser = User.objects.get(id=user_id)
    # generate edit forms based on user_level and whose page an admin is looking at
    editForm = EditForm(user=user) if user.user_level == 'user' else EditAdminForm(user=urlUser)
    editDescription = EditDescriptionForm(user=user) if user.id == int(user_id) else ''
    context = {
        'user': urlUser,
        'editForm': editForm,
        'editDescriptionForm': editDescription,
        'editPasswordForm': EditPasswordForm(),
    }
    return render(request, 'dashboard/edit.html', context)

# POST request for user editing info
def edit_info(request, user_id):
    editstatus = User.userManager.editInfo(user_id, **request.POST)
    # generate messages based on whether or not validation was successful
    if editstatus[0]:
        messages.success(request, editstatus[1])
    else:
        for message in editstatus[1]:
            messages.warning(request, message)
    return redirect(reverse('dashboard:edit', args=[user_id]))

# POST request for user editing password
def edit_pw(request, user_id):
    editstatus = User.userManager.editPassword(user_id, **request.POST)
    # generate messages based on whether or not validation was successful
    if editstatus[0]:
        messages.success(request, editstatus[1])
    else:
        for message in editstatus[1]:
            messages.warning(request, message)
    return redirect(reverse('dashboard:edit', args=[user_id]))

# POST request for user editing description
def edit_desc(request, user_id):
    editstatus = User.userManager.editDescription(user_id, request.POST['description'])
    # generate messages based on whether or not validation was successful
    if editstatus[0]:
        messages.success(request, editstatus[1])
    else:
        for message in editstatus[1]:
            messages.warning(request, message)
    return redirect(reverse('dashboard:edit', args=[user_id]))

# POST link for delete user link (admin only)
def remove_admin(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect(reverse('dashboard:index'))

# admin page to create new user
def new_admin(request):
    if not 'user_id' in request.session:
        return redirect(reverse('login:index'))
    if User.objects.get(id=request.session['user_id']).user_level == 'admin':
        context = {'regform': RegisterForm() }
        return render(request, 'dashboard/new_admin.html', context)
    else:
        return redirect(reverse('dashboard:index'))

# POST link for new user form (admin only)
def create_admin(request):
    create_status = User.userManager.register(**request.POST)
    if create_status[0]:
        return redirect(reverse('dashboard:index'))
    else:
        for message in create_status[1]:
            messages.warning(request, message)
        return redirect(reverse('login:new_admin'))

# show user wall
def show(request, user_id):
    if not 'user_id' in request.session:
        return redirect(reverse('login:index'))
    messages = Message.objects.filter(walluser=user_id).order_by('-id')
    comments = Comment.objects.all()
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'messages': messages,
        'comments': comments
    }
    return render(request, 'dashboard/show.html', context)
# POST request for adding message
def new_message(request, user_id):
    messageuser = User.objects.get(id=request.session['user_id'])
    walluser = User.objects.get(id=user_id)
    message = request.POST['message']
    Message.objects.create(messageuser=messageuser, walluser=walluser, message=message)
    return redirect(reverse('dashboard:show', args=user_id))

# POST request for adding comment
def new_comment(request, user_id, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    comment = request.POST['comment']
    Comment.objects.create(user=user, message=message, comment=comment)
    return redirect(reverse('dashboard:show', args=user_id))
