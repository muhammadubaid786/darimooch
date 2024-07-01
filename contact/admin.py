from django.contrib import admin
from .models import Contact
class contactAdmin(admin.ModelAdmin) :
    list_display = ['fullname' ,'email' ,'phone' , 'message']
    # products.objects.all()

admin.site.register(Contact ,contactAdmin)