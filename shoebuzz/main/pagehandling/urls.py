import imp
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingPage,name='landingPage'),
    path('bags',views.bagsPage,name='bagsPage'),
]