from django.shortcuts import render
from products.models import Products
def home(request) :
    productsdata = Products.objects.all()
    data = {
        "products" : productsdata
    }
    return render(request , 'index.html' , data)