from rest_framework import serializers
from authApp.models.portatil import Portatil


class PortatilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portatil
        fields = ['id', 'modelo', 'marca', 'fechaLanzamiento', 
                  'tamaño', 'precio', 'procesador', 'ram', 'rom', 'color',
                  'imagen']