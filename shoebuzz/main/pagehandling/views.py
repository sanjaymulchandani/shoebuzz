from django.urls import reverse
from django.shortcuts import redirect, render
from . forms import CustomUserCreationForm
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
def loginPage(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def homePage(request):
    return render(request,'home.html')

    #add products details from django admin page to your templates:
# def products(request):
#     products = Products.objects.all()
#     return render(request,'shoes.html',{'products':products})


def home(request):
    return redirect(request,'index.html')

def register(request):
    if request.method == "GET":
        return render(request,'register.html',{'form':CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse,("landingPage"))