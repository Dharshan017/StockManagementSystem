from django import forms
from django.db import transaction
from .models import Order
from django.contrib import messages 

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('OrderedProduct','OrderedQuantity','OrderedCustomer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['OrderedProduct'].label = 'Product Name'
        self.fields['OrderedQuantity'].label = 'Quantity'
        self.fields['OrderedCustomer'].label = 'Customer'

    def clean_OrderedQuantity(self):
        qty = self.cleaned_data['OrderedQuantity']
        prod = self.cleaned_data['OrderedProduct']
        if prod.AvailableQuantity<qty:
            raise forms.ValidationError('Invalid Quantity Entered!')
        return qty 

    @transaction.atomic
    def save(self):
        order = super().save(commit=False)
        if order.OrderedProduct.AvailableQuantity<order.OrderedQuantity:
            print('No Stock!')
        else:
            order.OrderedProduct.AvailableQuantity-=order.OrderedQuantity
            order.OrderedProduct.save()
            order.save()
        return order
        