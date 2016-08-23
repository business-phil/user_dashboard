from django.shortcuts import render, redirect
from django.views.generic import View

# user/admin home page
def index(request):
    current_user = User.objects.get(id=request.session['user_id'])
    user = User.objects.all()

    context = {
        'users' :user,
                }

    if current_user.user_level == 'user':
        return render(request, 'dashboard/index.html', context)
    else:
        return render(request, 'dashboard/index_admin.html', context)

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
    User.objects.filter(user_id=user_id).delete() 
    return redirect(reverse('dashboard:index_admin')) #after user is created - redirects to the admin user dashboard

# admin page to create new user
def new_admin(request):
    return render(request, 'dashboard/new_admin.html')
    
# POST link for new user form (admin only)
def create_admin(request): 
    User.objects.create(email= request.POST['email'], first_name = request.POST['first_name'], last_name= request.POST['last_name'], password= request.POST['password'])
    print Appointment.userManager.all()
    return redirect(reverse('dashboard:index_admin'))

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
