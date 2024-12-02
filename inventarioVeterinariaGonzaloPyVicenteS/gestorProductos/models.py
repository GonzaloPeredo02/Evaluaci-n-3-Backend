from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripción")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos', default=1)
    # vicente la ultima foreign key hace referencia al tipo usuario. 
    # justamente para diferenciarlos de el acceso que se dara.

    def __str__(self):
        return self.nombre


#vicente importante crear las migraciones 
# python manage.py makemigrations
# python manage.py migrate
# para importar las tablas a la base de datos


