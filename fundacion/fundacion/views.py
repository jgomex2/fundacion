#Definición de vistas
from django.shortcuts import render
from django.views.generic.edit import CreateView
from noticias.models import noticia


#página de inicio
def inicio(request):
    template_name = "index.html"
    noticias = noticia.objects.all()

    contexto={
        'noticia': noticias
    }
    return render(request,template_name,contexto)

#página de login
def login(request):
    return render(request,"login.html",{})

def logout(request):
    template_name = "index.html"
    contexto={}
    return render(request,template_name,contexto)

#class Registro(CreateView)