from rest_framework import serializers

from .models import *

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    courier_id = serializers.UUIDField(write_only=True)
    courier = CourierSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = '__all__'