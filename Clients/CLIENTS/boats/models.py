from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User



class Boat(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, )
    boat_name = models.CharField(max_length= 200)
    boat_description = models.CharField(max_length= 500)
    boat_price = models.IntegerField()
    photo = models.ImageField(upload_to='boats', null=True)
    brand = models.CharField(max_length= 200, null = True)
    year = models.IntegerField(null= True)

    def __str__(self):
        return self.boat_name



class Image(models.Model):
    boats = models.ManyToManyField(Boat)
    image = models.ImageField(upload_to='boats', null=True)

    

admin.site.register(Boat,)