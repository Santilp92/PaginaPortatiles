import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.portatilSerializer import PortatilSerializer
from authApp.models import Portatil
from rest_framework.views import APIView




# class ListaDetailView(views.APIView):

class ListaDetailView(APIView):
    def get(self, request, *args, **kwargs):
        lista = Portatil.objects.all()
        if not lista:
            return Response({"detail": "No existen portátiles en la base de datos"}, status=400)

        serializer = PortatilSerializer(lista, many=True)
        return Response(serializer.data)

    # def get(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         lista = Portatil.objects.all()
    #         if (not lista):
    #             return HttpResponseBadRequest("No existen personas en la bd")
    #         listaData = []
    #         for x in lista:
    #             data = {
    #                     "id":x.id,
    #                     "modelo": x.modelo,
    #                     "marca": x.marca,
    #                     "fechaLanzamiento": x.fechaLanzamiento.strftime('%Y-%m-%d'),
    #                     "tamaño": x.tamaño,
    #                     "precio": x.precio,
    #                     "procesador": x.procesador,
    #                     "ram": x.ram,
    #                     "rom": x.rom,
    #                     "color": x.color,
    #                     "imagen": x.imagen,
    #                     }
    #             listaData.append(data)
    #         dataJson = json.dumps(listaData)
    #         resp = HttpResponse()
    #         resp.headers['Content-Type'] = "text/json"
    #         resp.content = dataJson
    #         return resp
    #     else:
    #         return HttpResponseNotAllowed(['GET'], "Método inválido")

