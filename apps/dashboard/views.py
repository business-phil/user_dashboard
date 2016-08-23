from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse

# non-admin home page
def index(request):
    pass

# admin home page
def index_admin(request):
    pass

# users page to edit own info
def edit(request):
    pass

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
    messages = Message.objects.all()
    comments = Comment.objects.all()
    user = User.objects.get(id=user_id)
    context = {
        'user' = user,
        'messages' = messages,
        'comments' = comments
    }
    return render(request, 'dashboard/show.html')
# POST request for adding message
def new_message(request):  #POST REQUEST
    user = User.objects.get(id=request.session['user_id'])
    message = request.POST['message']
    Message.objects.create(user=user, message=message)
    return redirect(reverse('show'))

# POST request for adding comment
def new_comment(request, message_id):  #POST REQUEST
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    comment = request.POST['comment']
    Comment.objects.create(user=user, message=message, comment=comment)
    return redirect(reverse('show'))

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
