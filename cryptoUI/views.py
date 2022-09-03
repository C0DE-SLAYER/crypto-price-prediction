from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.
def index(request):
    return render(request, "index/index.html")

def SignUp(request):
    return render(request, "login/register.html")

def SignIn(request):
    return render(request, "login/login.html")

def signup(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if (form.password==form.password1):

            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                password1 = form.cleaned_data['password1']
                user = authenticate(username = username,password = password)
                login(request, user)
                return render(request,'index/index.html')
            
            else:
                return render(request,'login/login.html',{'form':form})
        else:
            HTTPResponse("password dosent matched.")
    else:
        form = UserCreationForm()
        return render(request,'login/login.html',{'form':form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request,'login/login.html',{'form':form})
    
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form':form})


def signout(request):
    # logout(request)
    return render(request, "login/login.html")