from django.contrib import admin
from django.urls import path
from cryptoUI import views
urlpatterns = [
    path("",views.index,name='index'),
    path('register', views.SignUp, name ='signup'),
    path('login', views.SignIn, name = 'signin'),
    path('signout', views.signout, name = 'logout'),
]