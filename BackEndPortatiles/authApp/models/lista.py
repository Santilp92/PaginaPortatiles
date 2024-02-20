from django.db import models
from .portatil import Portatil


class Lista(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.ForeignKey(Portatil, related_name = "Portatil", on_delete = models.CASCADE) 
    