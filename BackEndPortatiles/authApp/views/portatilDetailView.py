import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.portatil import Portatil
from authApp.serializers.portatilSerializer import PortatilSerializer


class PortatilDetailView(views.APIView):

    def get(self,request, pk):
        portatil = Portatil.objects.filter(id = pk)
        if not portatil:
            return HttpResponseBadRequest("No existe esta referencia")

        serializer = PortatilSerializer(portatil, many=True)
        return Response(serializer.data)


    # def get(self, request, pk):
    #     if (request.method == 'GET'):
            
    #         portatil = Portatil.objects.filter(id = pk)
    #         if (not portatil):
    #             return HttpResponseBadRequest("No existe esta referencia")
            
    #         for dato in portatil:
    #            data = {"id":dato.id,
    #                    "modelo":dato.modelo,
    #                    "marca":dato.marca,
    #                    "fechaLanzamiento": dato.fechaLanzamiento.strftime('%Y-%m-%d'),
    #                    "tamaño":dato.tamaño,
    #                    "precio":dato.precio,
    #                    "procesador":dato.procesador,
    #                    "ram":dato.ram,
    #                    "rom":dato.rom,
    #                    "color": dato.color,
    #                    "imagen":dato.imagen,                  
    #                 }
        
    #         dataJson = json.dumps(data)
    #         resp = HttpResponse()
    #         resp.headers['Content-Type'] = "text/json"
    #         resp.content = dataJson
    #         return resp
    #     else:
    #         return HttpResponseNotAllowed(['GET'], "Método inválido")   
        
    def put(self, request, pk):
        if request.method == 'PUT':
            portatil = Portatil.objects.filter(id = pk)
            if not portatil.exists():
                return HttpResponseBadRequest("No existe esta referencia")

            # Obtén el primer portátil de la consulta
            portatil = portatil.first()

            # Actualiza los datos del portátil con los datos proporcionados en la solicitud
            serializer = PortatilSerializer(portatil, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponseNotAllowed(['PUT'], "Método inválido")
        
    
    def patch(self, request, pk):
        if request.method == 'PATCH':
            portatil = Portatil.objects.filter(id=pk)
            if not portatil.exists():
                return HttpResponseBadRequest("No existe esta referencia")

            # Obtén el primer portátil de la consulta
            portatil = portatil.first()

            # Actualiza los datos del portátil con los datos proporcionados en la solicitud
            serializer = PortatilSerializer(portatil, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponseNotAllowed(['PATCH'], "Método inválido")
        
    def delete(self, request, pk):
        if request.method == 'DELETE':
            portatil = Portatil.objects.filter(id=pk)
            if not portatil.exists():
                return HttpResponseBadRequest("No existe esta referencia")

            # Obtén el primer portátil de la consulta y elimínalo
            portatil = portatil.first()
            portatil.delete()

            return Response("Portátil eliminado exitosamente", status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponseNotAllowed(['DELETE'], "Método inválido")


        