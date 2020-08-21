from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Client(models.Model):
    #Client
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = "")
    name = models.CharField(max_length=200, null = True, )
    phone = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)
    state  = models.CharField(max_length=200, null= True)

    #Current Boat
    model  = models.CharField(max_length=200, null= True)
    year =  models.IntegerField( null= True)
    location = models.CharField(max_length=200, null= True)
    equipment = models.CharField(max_length=2000, null= True)
    value = models.IntegerField(null= True)
    
    #Boat of interest
    model_interest  = models.CharField(max_length=200, null= True)
    year_interest =  models.IntegerField( null= True)
    equipment_interest = models.CharField(max_length=2000, null= True)
    budget = models.IntegerField( null= True)
    other_interests = models.CharField(max_length= 2000, null= True)
    
    #Communication
    first_contact = models.CharField(max_length=1000, null= True)
    to_contact = models.DateField(null = True)
    to_contact_text = models.CharField(max_length= 2000, null = True)
    communication = models.CharField(max_length=5000, null= True)
    importance = models.IntegerField( null= True)


class clientFile(models.Model):
    clients = models.ManyToManyField(Client)
    clientFile = CloudinaryField(folder = 'clientFiles', resource_type = "raw",null = True, use_filename = True)
    
