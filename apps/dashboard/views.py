from django.shortcuts import render, redirect
from django.views.generic import View

# non-admin home page
def index(request):
    pass

# admin home page
def index_admin(request):
    pass

# users page to edit own info
def edit(request):
    user = User.objects.get(id=request.session['user_id'])

    if user.user_level = 'user':
        editForm = EditForm()
        editPasswordForm = EditPasswordForm()
        editDescriptionForm = EditDescriptionForm()
        editStr = 'profile'
        title = 'Profile'
        #show div id=EditDescriptionForm

    else:
        editForm = EditAdminForm()
        editPasswordForm = EditPasswordAdminForm()
        editDescriptionForm = ''
        editStr = "user #" + str(request.session['user_id'])
        title = 'User'
        #hide div id= EditdescriptionForm

    context = {
        'editForm': editForm,
        'editPasswordForm': editPasswordForm,
        'editDescriptionForm': editDescriptionForm,
        'editStr': editStr,
        'title':title,
        #show/hide div id=EditDescriptionForm
    }
    return render(request, 'edit.html', context)

# POST request for user editing info
def edit_info(request):  #POST REQUEST
    pass

# POST request for user editing password
def edit_pw(request):  #POST REQUEST
    pass

# POST request for user editing description
def edit_desc(request):  #POST REQUEST
    pass

# admin page to edit other users info
def edit_admin(request, user_id):
    pass

# POST request for admin editing user info
def edit_info(request, user_id):  #POST REQUEST
    pass

# POST request for admin editing user password
def edit_pw(request, user_id):  #POST REQUEST
    pass

# POST link for delete user link (admin only)
def remove_admin(request, user_id):  #POST REQUEST
    pass

# admin page to create new user
def new_admin(request):
    pass

# POST link for new user form (admin only)
def create_admin(request):  #POST REQUEST
    pass

# show user wall
def show(request, user_id):
    pass

# POST request for adding message
def new_message(request):  #POST REQUEST
    pass

# POST request for adding comment
def new_comment(request, message_id):  #POST REQUEST
    pass

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
