from django.shortcuts import render
from .models import Client, clientFile
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
    
 
    
    return render(request, 'clients.html', { "clients" : clients, "user": user})

def signUpForm(request,):

    return render(request, 'signUpForm.html')
def addUser(request):
    username = request.POST["username"]
    password = request.POST.get("password")
    user =  User.objects.create_user( username = username, password = password, is_superuser = True)
    user.save()
    user = User.objects.get(username = request.POST["username"])

    
    return render(request, 'clients.html', { "user": user}) 

def profile(request, username):
    user = User.objects.get(username=username)
    
    context = {'username': username, 'user': user}
    return render(request, 'profile.html', context)

def addClient(request, username):
    user = User.objects.get(username = username)
    
    return render(request, 'addClient/addClient.html', {"user": user})

def addClient2(request, username):
    user = User.objects.get(username = username)
    
    #Client
    user = user
    name = request.POST.get('name')
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    state  = request.POST.get("state")

    #Current Boat
    model  = request.POST.get("model")
    year =  request.POST.get("year")
    location = request.POST.get("location")
    equipment = request.POST.get("equipment")
    value = request.POST.get("value")

    #Boat of interest
    model_interest = request.POST.get("model_interest")
    year_interest = request.POST.get("year_interest")
    equipment_interest = request.POST.get("equipment_interest")
    budget = request.POST.get("budget")
    other_interests = request.POST.get("other_interests")

    #Communication
    first_contact = request.POST.get("first_contact")
    to_contact = request.POST.get("to_contact")
    to_contact_text = request.POST.get("to_contact_text")
    communication = request.POST.get("communication")
    importance = request.POST.get("importance")
    
    

    Client.objects.create(user = user, name = name, phone = phone, email = email, state = state, 
    model = model, year = year, location = location, equipment = equipment, value = value,  
    model_interest = model_interest, year_interest = year_interest, 
    equipment_interest = equipment_interest, budget = budget, other_interests = other_interests, 
    first_contact = first_contact, to_contact = to_contact, to_contact_text = to_contact_text,
    communication = communication, importance = importance, )

    client = Client.objects.get(user = user, name = name, phone = phone, email = email, state = state,
     model = model, year = year, location = location, 
     budget = budget, first_contact = first_contact, to_contact = to_contact, to_contact_text = to_contact_text,
    communication = communication, importance = importance,)

    for file1 in request.FILES.getlist('files'):

        file2 = clientFile.objects.create( clientFile = file1 )
        file2.clients.add(client)
        file2.save()

    return redirect('home')

def clientDetails(request, id, username):
    
    user = User.objects.get(username = username)
    client = Client.objects.get(id = id, user = user)
    importance = client.importance
    
    if clientFile.objects.filter(clients = client):
        files = clientFile.objects.filter(clients = client)
    else: 
        files = None

    return render(request, 'clientDetails.html', {"client": client, "importance": importance, 'files': files, 'user': user})

def deleteClient(request, username, id):
    
    user = User.objects.get(username = username)

    Client.objects.get(id = id,  user = user).delete()

    return redirect('home')

def startClientDeletion(request, username, id):

    user = User.objects.get(username = username)
    client = Client.objects.get(user = user, id = id)

    return render(request, 'areYouSureClient.html', {"user": user, "client": client})
    
    
def filterClients(request, username):
    user = User.objects.get(username = username)

    return render(request, 'filters/filterClients.html', {'user': user})

def filterClients2(request, username):

    user = User.objects.get(username = username)
    clients = Client.objects.filter(user = user)

    #Ranges
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

    #Client
    if request.POST.get("name"):
        name = request.POST.get("name")
        clients = clients.filter( name__icontains = name)
    if request.POST.get("state"):
        state = request.POST.get("state")
        clients = clients.filter( state__icontains = state)

    #Current Boat
    if request.POST.get("model"):
        model = request.POST.get("model")
        clients = clients.filter( model__icontains = model)
    if request.POST.get("location"):
        location = request.POST.get("location")
        clients = clients.filter( location__icontains = location)
    
    #Future interest
    if request.POST.get("model_interest"):
        model_interest = request.POST.get("model_interest")
        clients = clients.filter( model_interest__icontains = model_interest)
    if request.POST.get("other_interests"):
        other_interests = request.POST.get("other_interests")
        clients = clients.filter( other_interests__icontains = other_interests)
    
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

def editClientInfo(request, id):
    
    username = request.POST["username"]
    user = User.objects.get(username = username)
    client = Client.objects.get(id = id, user = user)

    return render(request, 'editClientInfo.html', {'client': client, 'user': user})

def editClientInfo2(request, username):
    
    client_id = request.POST.get('id')
    user = User.objects.get(username = username)
    client = Client.objects.get(id= client_id, user = user)

    #Client
    client.name = request.POST.get('name')
    clientphone = request.POST.get("phone")
    client.email = request.POST.get("email")
    client.state  = request.POST.get("state")

    #Current boat
    client.model = request.POST.get("model")
    client.year =  request.POST.get("year")
    client.location = request.POST.get("location")
    client.equipment = request.POST.get("equipment")
    client.value = request.POST.get("value")
    
    #Boat of interest
    client.model_interest = request.POST.get("model_interest")
    client.year_interest = request.POST.get("year_interest")
    client.equipment_interest = request.POST.get("equipment_interest")
    client.budget = request.POST.get("budget")
    client.other_interests = request.POST.get("other_interests")

    #Communication
    client.first_contact = request.POST.get("first_contact")
    if request.POST.get("to_contact"):
        client.to_contact = request.POST.get("to_contact")
    client.to_contact_text = request.POST.get("to_contact_text")
    client.communication = request.POST.get("communication")
    client.importance = request.POST.get("importance")
    client.save()

    for file1 in request.FILES.getlist('files'):

        file2 = clientFile.objects.create( clientFile = file1 )
        file2.clients.add(client)
        file2.save()
    
    clients = Client.objects.filter(user = user)
    return redirect(home)