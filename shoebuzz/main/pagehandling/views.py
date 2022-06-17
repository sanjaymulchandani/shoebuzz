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


