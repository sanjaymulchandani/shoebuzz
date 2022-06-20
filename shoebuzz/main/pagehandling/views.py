from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
# Create your views here.
def landingPage(request):
    return render(request,'index.html')
def bagsPage(request):
    return render(request,'bags.html')
def clothingPage(request):
    return render(request,'clothing.html')
def shoesPage(request):
    return render(request,'shoes.html')
def salePage(request):
    return render(request,'sale.html')
def homePage(request):
    return render(request,'home.html')
def dashboard(request):
    return render(request,'dashboard.html')
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(request,'login/')
    form = UserCreationForm()
    return render (request,'register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect(reverse("login"))
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form}) 