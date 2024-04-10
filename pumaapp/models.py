from django.db import models

# Create your models here.

class Shoe(models.Model):
    
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    banner=models.ImageField(upload_to='pics')
    banner2=models.ImageField(upload_to='pics')
   
    
    def __str__(self):
        
        return self.name
    
