from rest_framework import views, viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .renderers import DataJSONRenderer
from .serializers import *

class CourierView(viewsets.ModelViewSet):
    serializer_class = CourierSerializer
    renderer_classes = (DataJSONRenderer,)
    queryset = Courier.objects.all()

    @action(detail=True, methods=['post'])
    def add_courier(self, request, pk=None):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ShipmentView(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer
    renderer_classes = (DataJSONRenderer,)
    queryset = Shipment.objects.all()

    @action(detail=True, methods=['post'])
    def add_shipment(self, request, pk=None):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

