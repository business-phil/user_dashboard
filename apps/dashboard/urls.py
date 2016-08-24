from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<user_id>\d+)$', views.edit, name='edit'),
    url(r'^edit_pw/(?P<user_id>\d+)$', views.edit_pw, name='edit_pw'),  #POST
    url(r'^edit_desc/(?P<user_id>\d+)$', views.edit_desc, name='edit_desc'),  #POST  
    url(r'^edit_info/(?P<user_id>\d+)$', views.edit_info, name='edit_info'),  #POST
    url(r'^remove/(?P<user_id>\d+)$', views.remove_admin, name='remove_admin'),  #POST
    url(r'^new$', views.new_admin, name='new_admin'),
    url(r'^create$', views.create_admin, name='create_admin'),  #POST
    url(r'^show/(?P<user_id>\d+)$', views.show, name='show'),
    url(r'^show/(?P<user_id>\d+)/new$', views.new_message, name="new_message"),  #POST
    url(r'^show/(?P<user_id>\d+)/(?P<message_id>\d+)/new$', views.new_comment, name="new_comment"),  #POST
]

'''
TO BE ADDED:
- user link to delete own message
- user link to delete own comment
'''
