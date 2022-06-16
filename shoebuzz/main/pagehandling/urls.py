import imp
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingPage,name='landingPage'),
    path('bags',views.bagsPage,name='bagsPage'),
    path('clothing',views.clothingPage,name='clothingPage'),
    path('sale',views.salePage,name='salePage'),
    path('shoes',views.shoesPage,name='shoesPage'),
    path('sports',views.sportsPage,name='sportsPage'),
    path('support',views.supportPage,name='supportPage'),
    path('login',views.loginPage,name='loginPage'),
    path('register',views.registerPage,name='registerPage'),    
]