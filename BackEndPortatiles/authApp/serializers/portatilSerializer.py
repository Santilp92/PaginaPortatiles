from rest_framework import serializers
from authApp.models.portatil import Portatil


class PortatilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portatil
        fields = ['referencia', 'nombre', 'marca', 'fechaLanzamiento', 
                  'tamaño', 'precio', 'procesador', 'ram', 'rom', 'sinopsis',
                  'imagen', 'foto1', 'foto2']

    # def get(self, obj):
    #     portatil = Portatil.objects.get(referencia=obj.referencia)
    #     return {
    #             'referencia': portatil.referencia,
    #             'nombre':portatil.nombre,
    #             'marca':portatil.marca,
    #             'fechaLanzamiento':portatil.fechaLanzamiento,
    #             'tamaño':portatil.tamaño,
    #             'precio':portatil.precio,
    #             'procesador':portatil.procesador,
    #             'ram':portatil.ram,
    #             'rom':portatil.rom,
    #             'sinopsis':portatil.sinopsis,
    #             'imagen':portatil.imagen,
    #             'foto1':portatil.foto1,
    #             'foto2':portatil.foto2,
    #             }