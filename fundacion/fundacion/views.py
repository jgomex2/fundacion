#Definición de vistas
from django.shortcuts import render
from django.views.generic.edit import CreateView

#página de inicio
def inicio(request):
    template_name = "index.html"
    contexto={}
    return render(request,template_name,contexto)

#página de login
def login(request):
    return render(request,"login.html",{})

#class Registro(CreateView)