from django.db import models

# Create your models here.
from django.contrib import auth

class User(auth.models.AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)


class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)