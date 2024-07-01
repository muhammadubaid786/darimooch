from django.db import models
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
   
    