from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.portatil import Portatil
from authApp.serializers.portatilSerializer import PortatilSerializer
from authApp.serializers.listaSerializer import ListaSerializer


class PortatilCreateView(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer = PortatilSerializer(data = request.data)

        if (serializer.is_valid(raise_exception=True)):
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


