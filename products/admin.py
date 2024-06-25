from django.contrib import admin
from .models import Products
class ProductAdmin(admin.ModelAdmin) :
    list_display = ['Title' ,'discription' , 'price' ,'category' ,'image' ]
    # products.objects.all()

admin.site.register(Products ,ProductAdmin)