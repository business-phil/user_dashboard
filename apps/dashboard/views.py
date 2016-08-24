from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from .models import User, Message, Comment
from .forms import RegisterForm, EditForm, EditAdminForm, EditPasswordForm, EditDescriptionForm

# user/admin home page
def index(request):
    current_user = User.objects.get(id=request.session['user_id'])
    user = User.objects.all()
    context = {
        'users' :user,
                }

    if current_user.user_level == 'user':
        return render(request, 'dashboard/index.html', context)
    else: #only two choices for user level - admin and user
        return render(request, 'dashboard/index_admin.html', context)

# users page to edit own info
def edit(request, user_id):
    #get the user object for whomever is in session
    user = User.objects.get(id=request.session['user_id'])

    #if the user_level is 'user', create the appropiate forms and strings
    if user.user_level == 'user':
        editForm = EditForm()
        editDescriptionForm = EditDescriptionForm()
        editStr = 'profile'
        title = 'Profile'
        #show div id=EditDescriptionForm
    #if the user_level is 'admin' and he is trying to edit himself
    #then create the appropiate forms and strings
    elif user.user_level == 'admin' and user.user_id == user_id:
        editForm = EditAdminForm()
        editDescriptionForm = EditDescriptionForm()
        editStr = 'profile'
        title = 'Profile'
        #hide div id= EditdescriptionForm
    #if the user_level is admin and he is trying to edit someone else
    #then create the appropiate forms and strings
    else:
        editForm = EditAdminForm()
        editDescriptionForm = ''
        editStr = "user #" + str(user_id)
        title = 'User'
        #hide div id= EditdescriptionForm
    #create editPasswordForm
    #NOTE: it is the same for admin and users
    editPasswordForm = EditPasswordForm()

    context = {
        'editForm': editForm,
        'editPasswordForm': editPasswordForm,
        'editDescriptionForm': editDescriptionForm,
        'editStr': editStr,
        'title':title,
        'user_id': user_id,
        #show/hide div id=EditDescriptionForm
    }
    return render(request, 'dashboard/edit.html', context)

# POST request for user editing info
def edit_info(request, user_id):  #POST REQUEST
    return redirect(reverse('dashboard:index'))
# POST request for user editing password
def edit_pw(request, user_id):  #POST REQUEST
    return redirect(reverse('dashboard:index'))

# POST request for user editing description
def edit_desc(request, user_id):  #POST REQUEST
    return redirect(reverse('dashboard:index'))

# admin page to edit other users info
def edit_admin(request, user_id):
    pass

# POST request for admin editing user info
def edit_info_admin(request, user_id):  #POST REQUEST
    pass

# POST request for admin editing user password
def edit_pw_admin(request, user_id):  #POST REQUEST
    pass

# POST link for delete user link (admin only)
def remove_admin(request, user_id):  #POST REQUEST
    User.objects.get(id= user_id).delete()
    return redirect(reverse('dashboard:index'))

# admin page to create new user
def new_admin(request):
    context = {'regform': RegisterForm }
    return render(request, 'dashboard/new_admin.html', context)

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
    messages = Message.objects.filter(walluser=user_id).order_by('-created_at')
    comments = Comment.objects.all()
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'messages': messages,
        'comments': comments
    }
    return render(request, 'dashboard/show.html', context)
# POST request for adding message
def new_message(request, user_id):  #POST REQUEST
    messageuser = User.objects.get(id=request.session['user_id'])
    walluser = User.objects.get(id=user_id)
    message = request.POST['message']
    Message.objects.create(messageuser=messageuser, walluser=walluser, message=message)
    return redirect(reverse('dashboard:show', args=user_id))

# POST request for adding comment
def new_comment(request, user_id, message_id):  #POST REQUEST
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    comment = request.POST['comment']
    Comment.objects.create(user=user, message=message, comment=comment)
    return redirect(reverse('dashboard:show', args=user_id))

'''
TO BE ADDED:
- class-based views
    ex: class New(View):
            def get(self, request):
                # renders new_admin.html
            def post(self, request):
                # processes POST request from FORM on new_admin.html

- user link to delete own message
- user link to delete own comment
'''
