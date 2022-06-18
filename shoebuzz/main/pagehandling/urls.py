from django.urls import path
from . import views
from django.conf.urls import include
urlpatterns = [
    path('',views.landingPage,name='landingPage'),
    path("accounts",include("django.contrib.auth.urls")),
    path('bags',views.bagsPage,name='bagsPage'),
    path('clothing',views.clothingPage,name='clothingPage'),
    path('sale',views.salePage,name='salePage'),
    path('shoes',views.shoesPage,name='shoesPage'),
    path('login/',views.loginPage,name='loginPage'),
    path('register/',views.registerPage,name="registerPage"),
    path('dashboard',views.dashboard,name="dashboard"),
]