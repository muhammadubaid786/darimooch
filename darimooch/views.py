from django.shortcuts import render
from products.models import Products
from carousel.models import carousel
def home(request) :
    productsdata = Products.objects.all()
    carouseldata = carousel.objects.all()
    data = {
        "products" : productsdata,
        "carousel" : carouseldata
    }
    return render(request , 'index.html' , data)