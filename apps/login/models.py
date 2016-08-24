from __future__ import unicode_literals
from django.db import models
from re import match, search
from bcrypt import hashpw, gensalt

class UserManager(models.Manager):
    def register(self, email, first_name, last_name, password, confirm_password, csrfmiddlewaretoken):
        messagelist = []
        # Validate email
        email = email[0]
        if not match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            messagelist.append("Invalid email address")
        elif User.objects.filter(email=email):
            messagelist.append("Email Address already in use")
        # Validate first_name
        first_name = first_name[0]
        if len(first_name) < 2:
            messagelist.append("First Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', first_name):
            messagelist.append("First Name must only contain letters")
        # Validate last_name
        last_name = last_name[0]
        if len(last_name) < 2:
            messagelist.append("Last Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', last_name):
            messagelist.append("Last Name must only contain letters")
        # Validate password
        password = password[0]
        if len(password) < 8:
            messagelist.append("Password must be at least 8 characters long")
        # Validate conf_password
        conf_password = confirm_password[0]
        if conf_password != password:
            messagelist.append("Password does not match")
        # Check if all validation checks passed
        if len(messagelist) == 0:
            pw_hash = hashpw(password.encode(), gensalt())
            # Make first registered user an admin
            if User.objects.all():
                new_user = User.objects.create(email=email, first_name=first_name, last_name=last_name, password=pw_hash)
            else:
                new_user = User.objects.create(email=email, first_name=first_name, last_name=last_name, password=pw_hash, user_level = 'admin')
            return (True, new_user.id)
        else:
            return (False, messagelist)
    def login(self, email, password):
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            if hashpw(password.encode(), user.password.encode()) == user.password:
                return (True, user.id)
            else:
                return (False, "Invalid password")
        else:
            return (False, "Invalid email address")

    def editInfo(self, user_id, email, first_name, last_name, csrfmiddlewaretoken, user_level=['user']):
        messageList = []
        #Validate email
        email = email[0]
        if not match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            messagelist.append("Invalid email address")
        # Validate first_name
        first_name = first_name[0]
        if len(first_name) < 2:
            messagelist.append("First Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', first_name):
            messagelist.append("First Name must only contain letters")
        # Validate last_name
        last_name = last_name[0]
        if len(last_name) < 2:
            messagelist.append("Last Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', last_name):
            messagelist.append("Last Name must only contain letters")
        
        user_level = user_level[0]
        #validations
        if len(messageList) > 0:
            return (False, messageList)

        self.filter(id=user_id).update(email=email, first_name=first_name, last_name=last_name, user_level=user_level)

        return (True, ["User Info updated successfully"])

    def editPassword(self, user_id, password, confirm_password, csrfmiddlewaretoken):
        messagelist = []
        # Validate password
        password = password[0]
        if len(password) < 8:
            messagelist.append("Password must be at least 8 characters long")
        # Validate conf_password
        conf_password = confirm_password[0]
        if conf_password != password:
            messagelist.append("Password does not match")
        # Check if all validation checks passed
        if len(messagelist) > 0:
            return(False, messagelist)

        pw_hash = hashpw(password.encode(), gensalt())

        self.filter(id=user_id).update(password=pw_hash)

        return (True, ["User Info updated successfully"])

    def editDescription(self, user_id, description):
        #no validations
        self.filter(id=user_id).update(description=str(description))
        return (True, ["Description Successfully Updated"])

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    user_level = models.CharField(
        max_length=5,
        choices=(('user', 'User'), ('admin', 'Admin')),
        default='user')
    description = models.TextField(max_length=400, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()
