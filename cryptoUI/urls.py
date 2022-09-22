
from django.urls import path
from cryptoUI import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register', views.registerPage, name ='register'),
    path('loginPage', views.loginPage, name = 'login'),
    path('signout', views.logoutPage, name = 'logout'),
]