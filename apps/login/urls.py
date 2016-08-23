from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.index, name="login"),  #POST
    url(r'^register$', views.register, name="register"),  #POST
]
