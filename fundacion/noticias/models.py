from django.db import models
from usuarios.models import Usuario

# Create your models here.

class categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Categoría")

class noticia(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    contenido = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria,null=True,blank=True,on_delete=models.CASCADE)


