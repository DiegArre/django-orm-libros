from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #autores = manytomany 

    def __repr___(self):
        return f"Titulo: {self.titulo}  Descripcion: {self.descripcion}"

    def __str__(self):
        return  f"Titulo: {self.titulo}  Descripcion: {self.descripcion}"
     

class Autor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    libros = models.ManyToManyField(Libro,related_name="autores")
    notas = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __repr___(self):
        return f"Nombre Autor:({self.first_name} {self.last_name})"

    def __str__(self):
        return  f"Nombre Autor:({self.first_name} {self.last_name})"