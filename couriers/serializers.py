from uuid import uuid4
from rest_framework import serializers

from .models import *

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res

class ShipmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentLog
        fields = '__all__'
