from django.db import models

class Portatil(models.Model):
    
    id = models.BigIntegerField(primary_key=True, blank=False)
    modelo = models.CharField(max_length = 50, blank=False)
    marca = models.CharField(max_length = 50, blank=False)
    fechaLanzamiento = models.DateField(blank=False)
    tamaño = models.DecimalField(max_digits = 5,decimal_places=2, default=0.0, blank=False)
    precio = models.BigIntegerField(default = 0, blank=False)
    procesador = models.CharField(max_length = 50)
    ram = models.SmallIntegerField(default = 0, blank=False)
    rom = models.SmallIntegerField(default=0, blank=False)
    color = models.CharField(max_length = 50, blank=False)
    imagen = models.ImageField(upload_to='media/')

    # sinopsis = models.CharField(max_length = 250)
    # imagen = models.ImageField(upload_to="media/", null =True, blank= True)
   


