import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.portatil import Portatil
from authApp.serializers.portatilSerializer import PortatilSerializer


class PortatilDetailView(views.APIView):

    def get(self, request, pk):
        if (request.method == 'GET'):
            
            portatil = Portatil.objects.filter(referencia = pk)
            if (not portatil):
                return HttpResponseBadRequest("No existe esta referencia")
            
            for dato in portatil:
               data = {"referencia":dato.referencia,
                       "nombre":dato.nombre,
                       "marca":dato.marca,
                       "tamaño":dato.tamaño,
                       "precio":dato.precio,
                       "procesador":dato.procesador,
                       "ram":dato.ram,
                       "rom":dato.rom,
                       "sinopsis":dato.sinopsis                  
                    }
        
            dataJson = json.dumps(data)
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = dataJson
            return resp
        else:
            return HttpResponseNotAllowed(['GET'], "Método inválido")   


        