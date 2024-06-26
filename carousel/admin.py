from django.contrib import admin
from .models import carousel
class carouselAdmin(admin.ModelAdmin) :
    list_display = ['Title' ,'discription' ,'image' ]
    # products.objects.all()

admin.site.register(carousel ,carouselAdmin)
# Register your models here.
