from django.contrib import admin

# Register your models here.
from .models import Brand,Product,Category,Order

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)