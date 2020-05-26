from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Boat(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, )
    owner = models.CharField(max_length = 200, null = True)
    brand = models.CharField(max_length= 200, null = True)
    model = models.CharField(max_length = 200, null = True)
    size = models.IntegerField( null = True)
    year = models.IntegerField(null= True)
    engine = models.CharField(max_length= 200, null = True)
    engine_hours = models.IntegerField( null = True)
    equipment = models.CharField(max_length= 1000, null = True)
    price = models.CharField(max_length=200, null = True)
    location = models.CharField(max_length= 200, null = True)
    photo = CloudinaryField(folder = 'boats', null = True)
    
    description = models.CharField(max_length=2000, null = True)

    def __str__(self):
        return self.boat_name



class Image(models.Model):
    boats = models.ManyToManyField(Boat)
    image = CloudinaryField(folder = 'boats', null = True)

    

admin.site.register(Boat,)