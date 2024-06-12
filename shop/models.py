from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50, default = '')
    subcategory = models.CharField(max_length=50, default = '')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=10,default='')
    issue = models.CharField(max_length=40,default='')
    query = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name
    

