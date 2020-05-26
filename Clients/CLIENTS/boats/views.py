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
import cloudinary


def boatsHome(request, username):
    user = User.objects.get(username = username)
    boats = Boat.objects.filter(user = user)
    return render(request, 'boats.html', {'user': user, 'boats': boats,})


def addBoat(request, username):

    return render(request, 'addBoat/addBoat.html', {'username': username})


def addBoat2(request, username):
    user = User.objects.get(username = username)
   
    photoslist = request.FILES.getlist('photos')
    
    owner = request.POST["owner"]
    brand = request.POST["brand"]
    model = request.POST.get("model")
    size = request.POST["size"]
    year = request.POST["year"]
    engine = request.POST["engine"]
    engine_hours = request.POST["engine_hours"]
    equipment = request.POST["equipment"]
    price = request.POST["price"]
    location = request.POST["location"]
    description = request.POST["description"]
    photo = request.FILES.get('photo')
    
    Boat.objects.create(user= user, owner = owner, brand = brand, model = model, 
        size = size, year = year, engine = engine, engine_hours = engine_hours, 
        equipment = equipment, price = price, location = location, photo = photo, 
        description = description)

    boat = Boat.objects.get(user= user, brand = brand, model = model, year = year, location = location,)
    

    
    for photo in request.FILES.getlist('photoslist'):
        
        image = Image.objects.create( image = photo)
        image.boats.add(boat)
        image.save()
    
    

    

    return redirect('boatsHome', username = username)


    
def boat_details(request, username, model):
    
    user = User.objects.get(username = username)
    boat = Boat.objects.get(user = user, model = model)
    if Image.objects.filter(boats = boat):
        images = Image.objects.filter(boats = boat)
    else: 
        images = None
    
    return render(request, "boat_details.html", {"boat": boat, 'images': images})

def deleteBoat(request, username, model):
    user = User.objects.get(username= username)
    boats = user.boat_set.all()
    boats = boats.filter(model = model)
    boats.delete()
    return redirect('boatsHome', username = username) 

def filterBoats2(request, username):
    user = User.objects.get(username = username)
    boats = Boat.objects.filter(user = user)


    if request.POST.get("owner"):
        owner = request.POST.get("owner")
        boats = boats.filter( owner__icontains = owner)

    if request.POST.get("brand"):
        brand = request.POST.get("brand")
        boats = boats.filter( brand__icontains = brand )

    if request.POST.get("model"):
        boat_name = request.POST.get("model")
        boats = boats.filter( model__icontains = boat_name)

    if request.POST.get("location"):
        location= request.POST.get("location")
        boats = boats.filter( location__icontains = location)

    if request.POST.get("engine"):
        engine = request.POST.get("engine")
        boats = boats.filter( engine__icontains = engine)

    if request.POST.get("equipment"):
        equipment = request.POST.get("equipment")
        boats = boats.filter( equipment__icontains = equipment)
    
    if request.POST.get("size_min") and request.POST.get("size_max"):
        size_min = request.POST.get("size_min")
        size_max = request.POST.get("size_max")
        boats = boats.filter(size__range = (size_min, size_max) )

    if request.POST.get("year_min") and request.POST.get("year_max"):
        year_min = request.POST.get("year_min")
        year_max = request.POST.get("year_max")
        boats = boats.filter(year__range = (year_min, year_max))

    if request.POST.get("engine_hours_min") and request.POST.get("engine_hours_max"):
        engine_hours_min = request.POST.get("engine_hours_min")
        engine_hours_max = request.POST.get("engine_hours_max")
        boats = boats.filter(engine_hours__range = (engine_hours_min, engine_hours_max))

    if request.POST.get("price_min") and request.POST.get("price_max"):
        price_min = request.POST.get("price_min")
        price_max = request.POST.get("price_max")
        boats = boats.filter(price__range = (price_min, price_max) )

    return render(request, 'filters/filtered_boats.html', { 'username': username, 'boats': boats})

def filterBoats(request, username):
    return render(request, 'filters/filterBoats.html', {'username': username })

def editBoat2(request, username):

    boat_id = request.POST.get('boat_id')
    user = User.objects.get(username= username)
    boat = Boat.objects.get(id = boat_id, user = user)

    if request.POST["owner"]!= boat.owner:
        boat.owner = request.POST["owner"]

    if request.POST.get("brand")!= boat.brand:
        boat.brand = request.POST["brand"]

    if request.POST.get("model")!= boat.model:
        boat.model = request.POST.get("model")

    if request.POST["size"]!= boat.size:
        boat.size = request.POST["size"]

    if request.POST["year"]!= boat.year: 
        boat.year = request.POST["year"]

    if request.POST["engine"]!= boat.engine:    
        boat.engine = request.POST["engine"]

    if request.POST["engine_hours"]!= boat.engine_hours:
        boat.engine_hours = request.POST["engine_hours"]

    if request.POST["equipment"]!= boat.equipment:
        boat.equipment = request.POST["equipment"]
    
    if request.POST["price"]!= boat.price: 
        boat.price = request.POST["price"]

    if request.POST["location"]!= boat.location:
        boat.location = request.POST["location"]

    if request.POST.get("description")!= boat.description: 
        boat.description = request.POST.get("description")


    
    if request.FILES.getlist('photos'):
        photoslist = request.FILES.getlist('photos')

        for photo in request.FILES.getlist('photoslist'):
        
            image = Image.objects.create( image = photo)
            image.boats.add(boat)
            image.save()

    boat.save()
    

    return redirect('boatsHome', username = username )