from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Boat, Image



def boatsHome(request, username):
    user = User.objects.get(username = username)
    boats = Boat.objects.filter( user = user)
    
    
    return render(request, 'boats.html', {'user': user, 'boats': boats,})


def addBoat(request, username):

    return render(request, 'addBoat/addBoat.html', {'username': username})


def addBoat2(request, username):
    user = User.objects.get(username = username)
    photo = request.FILES.get('photo')
    photoslist = request.FILES.getlist('photos')
    boat_name= request.POST["boat_name"]
    boat_description = request.POST["boat_description"]
    boat_price = request.POST["boat_price"]
    Boat.objects.create(user= user, boat_name = boat_name, boat_description=boat_description, boat_price = boat_price, photo = photo)
    boat = Boat.objects.get(user= user, boat_name = boat_name, boat_description=boat_description, boat_price = boat_price)
    
    
    for photo in request.FILES.getlist('photoslist'):
        
        image = Image.objects.create( image = photo)
        image.boats.add(boat)
        image.save()
    
    

    

    return redirect('boatsHome', username = username)


    
def boat_details(request, username, boat_name):
    
    user = User.objects.get(username = username)
    boat = Boat.objects.get(user = user, boat_name= boat_name)
    if Image.objects.filter(boats = boat):
        images = Image.objects.filter(boats = boat)
    else: 
        images = None
    
    return render(request, "boat_details.html", {"boat": boat, 'images': images})

def deleteBoat(request, username, boat_name):
    user = User.objects.get(username= username)
    boats = user.boat_set.all()
    boats = boats.filter(boat_name = boat_name)
    boats.delete()
    return redirect('boatsHome', username = username) 

def filterBoats2(request, username):
    user = User.objects.get(username = username)
    boats = Boat.objects.filter(user = user)
    if request.POST.get("boat_name"):
        boat_name = request.POST.get("boat_name")
        boats = boats.filter( boat_name__icontains = boat_name)
    return render(request, 'filters/filtered_boats.html', { 'username': username, 'boats': boats})