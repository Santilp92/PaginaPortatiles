import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.portatilSerializer import PortatilSerializer
from authApp.models import Portatil




class ListaDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            lista = Portatil.objects.all()
            if (not lista):
                return HttpResponseBadRequest("No existen personas en la bd")
            listaData = []
            for x in lista:
                data = {
                        "referencia":x.referencia,
                        "nombre": x.nombre,
                        "marca": x.marca,
                        "tamaño": x.tamaño,
                        "procesador": x.procesador,
                        "ram": x.ram,
                        "rom": x.rom,
                        "precio": x.precio,
                        }
                listaData.append(data)
            dataJson = json.dumps(listaData)
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = dataJson
            return resp
        else:
            return HttpResponseNotAllowed(['GET'], "Método inválido")

