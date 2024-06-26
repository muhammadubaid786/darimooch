from django.db import models
class carousel(models.Model):
    Title = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.FileField(max_length=60 , upload_to= "carousel/" , null=True)
    
# Create your models here.
