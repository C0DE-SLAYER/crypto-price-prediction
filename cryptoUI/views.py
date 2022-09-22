from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cryptoUI.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index/index.html')

def registerPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form=RegistrationForm()
    context={'form':form}
    return render(request, 'login/register.html',context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        myuser=authenticate(request, username=username,password=password)
        
        if myuser is not None:
            login(request, myuser)
            return redirect('index')
        else:
            messages.error(request,"sucessfully register")
            return redirect('login')

    return render(request, 'login/login.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('login')