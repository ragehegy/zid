from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .renderers import DataJSONRenderer
from .serializers import *

from utils.Courier import COURIERS_MAP

class CourierView(viewsets.ModelViewSet):
    serializer_class = CourierSerializer
    renderer_classes = (DataJSONRenderer,)
    queryset = Courier.objects.all()

    @action(detail=True, methods=['POST'])
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

    def get_courier_class(self, pk):
        courier = Shipment.objects.get(pk=pk).courier.name
        return COURIERS_MAP.get(courier, None)

    @action(detail=True, methods=['POST'])
    def add_shipment(self, request, pk=None):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['GET'])
    def print_label(self, request, pk=None):
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        courier = self.get_courier_class(pk)(serializer=serializer)
        return courier.print_label()

    @action(detail=True, methods=['GET'])
    def track_shipment(self, request, pk):
        courier = self.get_courier_class(pk)
        shipment = self.get_object()
        
        serializer = self.serializer_class(shipment)
        courier = courier(serializer)
        status = courier.get_shipment_status(shipment.status)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['GET'])
    def cancel_shipment(self, request, pk):
        shipment = self.get_object()
        shipment.cancel()
        serializer = self.serializer_class(shipment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
