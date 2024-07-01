from django.shortcuts import render
from products.models import Products
from carousel.models import carousel
from contact.models import Contact
def home(request) :
    productsdata = Products.objects.all()
    carouseldata = carousel.objects.all()
    data = {
        "products" : productsdata,
        "carousel" : carouseldata
    }
    return render(request , 'index.html' , data)
def contact(request) :
    name = request.GET.get('fullname')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    message = request.GET.get('message')

    contacts = Contact(fullname = name , email = email , phone = phone , message = message)
    contacts.save()
    return render(request , 'contact.html')