from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import login,authenticate
# Create your views here.

def landing_page(request):
    redirect (request,'templates/index.html')

def login_page(request):
    form = forms.loginForm()
    if request.method == "POST":
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                message = f'Hello {user.username}! You have been Logged in'
            else:
                message = 'Login Failed'
    return render(request,'templates/login.html',context={'form':form, 'message':message})
