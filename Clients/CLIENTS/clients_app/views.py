from django.shortcuts import render
from .models import Client, ClientForm, clientFile
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
import datetime
# Create your views here.

@login_required
def home(request,):
    username = request.user.username
    user = User.objects.get(username = username)
    clients = Client.objects.filter(user = user)
    
    form = ClientForm()
    
    return render(request, 'clients.html', {"form": form, "clients" : clients, "user": user})

def signUpForm(request,):

    return render(request, 'signUpForm.html')
def addUser(request):
    username = request.POST["username"]
    password = request.POST.get("password")
    user =  User.objects.create_user( username = username, password = password, is_superuser = True)
    user.save()
    user = User.objects.get(username = request.POST["username"])

    form = ClientForm()
    return render(request, 'clients.html', {"form": form, "user": user}) 

def profile(request, username):
    user = User.objects.get(username=username)
    
    context = {'username': username, 'user': user}
    return render(request, 'profile.html', context)

def addClient(request, username):
    user = User.objects.get(username = username)
    
    return render(request, 'addClient/addClient.html', {"user": user})

def addClient2(request, username):
    user = User.objects.get(username = username)
    
    user = user
    name = request.POST.get('name')
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    state  = request.POST.get("state")
    brand  = request.POST.get("brand")
    model = request.POST.get("model")
    year =  request.POST.get("year")
    location = request.POST.get("location")
    description = request.POST.get("description")
    look1 = request.POST.get("look1")
    look2 = request.POST.get("look2")
    budget = request.POST.get("budget")
    first_contact = request.POST.get("first_contact")
    to_contact_text = request.POST.get("to_contact_text")
    communication = request.POST.get("communication")
    importance = request.POST.get("importance")
    to_contact = request.POST.get("to_contact")
    

    Client.objects.create(user = user, name = name, phone = phone, email = email, state = state,
    brand = brand, model = model, year = year, location = location, description = description,
    look1 = look1, look2 = look2, budget = budget, first_contact = first_contact, to_contact = to_contact, to_contact_text = to_contact_text,
    communication = communication, importance = importance, )

    client = Client.objects.get(user = user, name = name, phone = phone, email = email, state = state,
    brand = brand, model = model, year = year, location = location, description = description,
    look1 = look1, look2 = look2, budget = budget, first_contact = first_contact, to_contact = to_contact, to_contact_text = to_contact_text,
    communication = communication, importance = importance,)

    for file1 in request.FILES.getlist('files'):

        file2 = clientFile.objects.create( clientFile = file1 )
        file2.clients.add(client)
        file2.save()

    return redirect('home')

def clientDetails(request, name):
    username = request.POST.get("username")
    user = User.objects.get(username = username)
    client = Client.objects.get(name = name, user = user)
    importance = client.importance

    if clientFile.objects.filter(clients = client):
        files = clientFile.objects.filter(clients = client)
    else: 
        files = None

    return render(request, 'clientDetails.html', {"client": client, "importance": importance, 'files': files, 'user': user})

def deleteClient(request, name):
    Client.objects.get(name = name).delete()

    return redirect('home')
    
def filterClients(request, username):
    user = User.objects.get(username = username)

    return render(request, 'filters/filterClients.html', {'user': user})

def filterClients2(request, username):

    user = User.objects.get(username = username)
    clients = Client.objects.filter(user = user)

    
    if request.POST.get("budget_min") and request.POST.get("budget_max"):
        min_budget = request.POST.get("budget_min")
        max_budget = request.POST.get("budget_max")
        clients = clients.filter( budget__range = (min_budget, max_budget), user = user)
    if request.POST.get("year_min") and request.POST.get("year_max"):
        year_min = request.POST.get("year_min")
        year_max = request.POST.get("year_max")
        clients = clients.filter( year__range = (year_min, year_max))
    if request.POST.get("importance_min") and request.POST.get("importance_max"):
        importance_min = request.POST.get("importance_min")
        importance_max = request.POST.get("importance_max")
        clients = clients.filter( importance__range = (importance_min, importance_max))
    if request.POST.get("state"):
        state = request.POST.get("state")
        clients = clients.filter( state__icontains = state)
    if request.POST.get("location"):
        location = request.POST.get("location")
        clients = clients.filter( location__icontains = location)
    if request.POST.get("brand"):
        brand = request.POST.get("brand")
        clients = clients.filter( brand__icontains = brand)
    if request.POST.get("model"):
        model = request.POST.get("model")
        clients = clients.filter( model__icontains = model)
    if request.POST.get("name"):
        name = request.POST.get("name")
        clients = clients.filter( name__icontains = name)
    
    return render(request, 'filters/filtered_clients.html', {'clients': clients} )


def filterClientsDay(request, username):
    user = User.objects.get(username = username)
    clients = Client.objects.filter (user = user, to_contact = datetime.date.today())
    
    return render(request, 'filters/filtered_clients.html', {'clients': clients} )

def filterClientsWeek(request, username):
    user = User.objects.get(username = username)
    date = datetime.date.today()
    end_week = date + datetime.timedelta(7)
    clients = Client.objects.filter (user = user, to_contact__range = (date, end_week))
    
    return render(request, 'filters/filtered_clients.html', {'clients': clients} )

def UserProfile(request, username):
    user = User.objects.get(username = username)
    return render(request, 'profile.html', {'user': user})

def editClientInfo(request, name):
    username = request.POST["username"]
    user = User.objects.get(username = username)
    client = Client.objects.get(name = name, user = user)

    return render(request, 'editClientInfo.html', {'client': client, 'user': user})

def editClientInfo2(request, username):
    
    client_id = request.POST.get('id')
    user = User.objects.get(username = username)
    client = Client.objects.get(id= client_id, user = user)

    client.name = request.POST.get('name')
    clientphone = request.POST.get("phone")
    client.email = request.POST.get("email")
    client.state  = request.POST.get("state")
    client.brand  = request.POST.get("brand")
    client.model = request.POST.get("model")
    client.year =  request.POST.get("year")
    client.location = request.POST.get("location")
    client.description = request.POST.get("description")
    client.look1 = request.POST.get("look1")
    client.look2 = request.POST.get("look2")
    client.budget = request.POST.get("budget")
    client.first_contact = request.POST.get("first_contact")
    client.to_contact_text = request.POST.get("to_contact_text")
    client.communication = request.POST.get("communication")
    client.importance = request.POST.get("importance")
    client.to_contact = request.POST.get("to_contact")
    client.save()
    
    clients = Client.objects.filter(user = user)
    return redirect(home)