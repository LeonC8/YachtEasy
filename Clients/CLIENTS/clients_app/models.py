from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = "")
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)
    state  = models.CharField(max_length=200, null= True)
    brand  = models.CharField(max_length=200, null= True)
    model = models.CharField(max_length=200, null= True)
    year =  models.IntegerField( null= True)
    location = models.CharField(max_length=200, null= True)
    description = models.CharField(max_length=2000, null= True)
    look1 = models.CharField(max_length=500, null= True)
    look2 = models.CharField(max_length=500, null= True)
    budget = models.IntegerField( null= True)
    first_contact = models.CharField(max_length=1000, null= True)
    to_contact = models.CharField(max_length=500, null= True)
    communication = models.CharField(max_length=5000, null= True)
    importance = models.IntegerField( null= True)

class ClientForm(ModelForm):
    class Meta:
        model = Client
        
        fields = ['user', 'name', 'phone', 'email', 'state', 'brand', 'model', 'year', 'location', 'description', 'look1', 'look2', 'budget','first_contact', 'to_contact', 'communication', 'importance' ]