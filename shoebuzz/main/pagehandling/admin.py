from django.contrib import admin
from . models import Products
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
admin.site.register(Products,productAdmin)