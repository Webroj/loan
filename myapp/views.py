from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_signup(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Congratulations Signup Successfully!!')
            fm.save()
            return HttpResponseRedirect('login')
            fm=UserCreationForm()
    else:
        fm=UserCreationForm()
    return render(request, 'signup.html', {'form':fm})

def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            myuser=authenticate(username=uname, password=upass)
            if myuser is not None:
                login(request, myuser)
                messages.success(request, 'Logged in Successfully !!')
                return HttpResponseRedirect('/about')
    else:
        fm=AuthenticationForm()
    return render(request, 'login.html', {'form':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def post_job(request):
    return render(request, 'post.html')

def want_job(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

