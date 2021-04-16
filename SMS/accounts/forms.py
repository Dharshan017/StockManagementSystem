from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Admin,Manager

class ManagerCreateForm(UserCreationForm):
    class Meta():
        fields = ('username','email','password1','password2')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager=True
        user.save()
        Manager.objects.create(user=user)
        return user
        
class AdminCreateForm(UserCreationForm):
    class Meta():
        fields = ('username','email','password1','password2')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin=True
        user.save()
        Admin.objects.create(user=user)
        return user