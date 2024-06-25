from django.db import models
class Products(models.Model):
    Title = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=60)
    image = models.FileField(max_length=60 , upload_to= "products/" , null=True)
    
    
