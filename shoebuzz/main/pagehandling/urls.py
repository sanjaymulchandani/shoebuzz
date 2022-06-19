from django.urls import path
from . import views
from django.conf.urls import include
urlpatterns = [
    path('',views.landingPage,name='landingPage'),
    path('bags',views.bagsPage,name='bagsPage'),
    path('clothing',views.clothingPage,name='clothingPage'),
    path('sale',views.salePage,name='salePage'),
    path('shoes',views.shoesPage,name='shoesPage'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('cart',views.cart,name="cart"),
    path('signup',views.signup_view,name="signup"),
    path('login',views.login_view,name="login"),
]