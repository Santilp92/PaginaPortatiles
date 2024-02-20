from django.db import models

class Portatil(models.Model):
    referencia = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 50)
    fechaLanzamiento = models.DateField()
    tamaño = models.SmallIntegerField(default=0)
    precio = models.BigIntegerField(default = 0)
    procesador = models.CharField(max_length = 50)
    ram = models.SmallIntegerField(default = 0)
    rom = models.SmallIntegerField(default=0)
    sinopsis = models.CharField(max_length = 250)
    imagen = models.ImageField(upload_to="media/", null =True, blank= True)
    foto1 = models.ImageField(upload_to="media/", null =True, blank= True)
    foto2 = models.ImageField(upload_to="media/", null =True, blank= True)
   


