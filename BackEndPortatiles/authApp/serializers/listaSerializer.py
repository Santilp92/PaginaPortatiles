from authApp.models.lista import Lista
from rest_framework import serializers
from authApp.models.lista import Lista
from authApp.models.portatil import Portatil
from authApp.serializers.portatilSerializer import PortatilSerializer


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ['id', 'modelo']


    def create(self, validated_data):
        portatilData = validated_data.pop('referencia')
        portatilInstance = Portatil.objects.get(**portatilData)
        Lista.objects.create(modelo= portatilInstance, **validated_data)
        return portatilInstance
        

    def to_representation(self, obj):
        portatil = Portatil.objects.get(id =obj.modelo)
        lista = Lista.objects.get(list=obj.id)
        return {
                'id': lista.id,
                'modelo': {
                    'nombre': portatil.nombre, 
                    'marca': portatil.marca,
                    'tamaño':portatil.tamaño,
                    'precio':portatil.precio,
                    'procesador':portatil.procesador,
                    'ram':portatil.ram,
                    'rom': portatil.rom,                   
                    }
                }