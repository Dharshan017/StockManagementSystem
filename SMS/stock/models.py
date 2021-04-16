from django.db import models

# from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()
# from django import template
# register = template.Library()
from django.urls import reverse
from django.utils import timezone
Availability = (
    ('1','Available'),
    ('2','UnAvailable'),
)

class Brand(models.Model):
    Brandname = models.CharField(max_length=256,primary_key=True)
    Brandstatus = models.CharField(max_length=256,choices = Availability,default=Availability[1][1])
    class Meta:
      ordering = ['Brandname']

    def __str__(self):
        return self.Brandname
      
    def get_absolute_url(self):
        return reverse('stock:list_brand')#, kwargs={'pk': self.pk})

class Category(models.Model):
    Categoryname = models.CharField(max_length=256,primary_key=True)
    Categorystatus = models.CharField(max_length=256,choices = Availability,default=Availability[1][1])
    class Meta:
      ordering = ['Categoryname']

    def __str__(self):
        return self.Categoryname
    
    def get_absolute_url(self):
        return reverse('stock:list_category')#, kwargs={'pk': self.pk})

class Product(models.Model):
    Productname = models.CharField(max_length=256,primary_key=True)
    Productstatus = models.CharField(max_length=256,choices = Availability,default=Availability[1][1])
    ProductBrand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='product_brand')
    ProductCategory = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product_category')
    AvailableQuantity = models.PositiveIntegerField(default=0)

    class Meta:
      ordering = ['Productname']

    def __str__(self):
        return self.Productname

    def get_absolute_url(self):
        return reverse('stock:list_product')#, kwargs={'pk': self.pk})

class Order(models.Model):
    OrderedProduct = models.ForeignKey(Product,on_delete=models.CASCADE)
    OrderedQuantity = models.PositiveIntegerField(default=1)
    OrderedCustomer = models.CharField(max_length=256,unique=False)
    OrderedDate = models.DateTimeField(default=timezone.now)

    class Meta():
        ordering = ['-OrderedDate']

    def __str__(self):
        return self.OrderedProduct_id+' '+str(self.OrderedQuantity)

    def get_absolute_url(self):
        return reverse('stock:list_order')#, kwargs={'pk': self.pk})