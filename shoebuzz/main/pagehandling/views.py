from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request,'index.html')
def bagsPage(request):
    return render(request,'bags.html')
def clothingPage(request):
    return render(request,'clothing.html')
def shoesPage(request):
    return render(request,'shoes.html')
def sportsPage(request):
    return render(request,'sports.html')
def salePage(request):
    return render(request,'sale.html')
def supportPage(request):
    return render(request,'support.html')
def loginPage(request):
    return render(request,'login.html')
def registerPage(request):
    return render(request,'register.html')