"""CLIENTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clients_app.views import home, addUser, profile, addClient, addClient2, clientDetails, deleteClient, filterClients, filterClients2
from boats.views import boatsHome, addBoat, addBoat2, boat_details, deleteBoat, filterBoats2
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('addUser', addUser, name="addUser"),
    path('<str:username>/profile/', profile, name="profile"),
    path('<str:username>/addClient', addClient, name = "addClient"),
    path('<str:username>/addClient2', addClient2, name = "addClient2"),
    path ('<str:name>/clientDetails', clientDetails, name = "clientDetails"),
    path('<str:name>/deleteClient', deleteClient, name = "deleteClient"),
    path ('<str:username>/boats_home', boatsHome, name = "boatsHome"),
    path ('<str:username>/addBoat', addBoat, name = "addBoat"),
    path ('<str:username>/addBoat2', addBoat2, name = "addBoat2"),
    path ('<str:username>/filterClients', filterClients, name = "filterClients"),
    path ( '<str:username>/<str:boat_name>/details', boat_details, name = "boat_details"),
    path ('<str:username>/filterClients2', filterClients2, name = "filterClients2"),
    path('<str:username>/<str:boat_name>/deleteBoat)', deleteBoat, name = "deleteBoat"),
    path('<str:username>/filterBoats2', filterBoats2, name = "filterBoats2")
     
]  + static(settings.STATIC_URL,)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)