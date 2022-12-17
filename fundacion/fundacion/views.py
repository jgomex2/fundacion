#Definición de vistas
from django.shortcuts import render


#página de inicio
def inicio(request):
    template_name = "index.html"
    contexto={}
    return render(request,template_name,contexto)