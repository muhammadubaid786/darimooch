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
    return render(request , 'contact.html')
def contact_save(request) :
    try :
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name == '' or email == '' or phone == '' or message == '' :
            return render(request , 'contact.html')
        contacts = Contact(fullname = name , email = email , phone = phone , message = message)
        contacts.save()
    except : 
        print('error')
    return render(request , 'contact.html')
    
def searchResult(request) :
    searchTerm = request.GET['search']
    searchitem = Products.objects.filter(Title__icontains = searchTerm)
    data = {
        "products" : searchitem,
    }

    return render(request , 'search.html' , data)