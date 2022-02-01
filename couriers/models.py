from uuid import uuid4

from django.db import models
from django.utils import timezone

SHIPMENT_STATUS = (
    ('REQUESTED', 'REQUESTED'),
    ('APPROVED', 'APPROVED'),
    ('REJECTED', 'REJECTED'),
    ('READ_TO_PICK', 'READ_TO_PICK'),
    ('PICKED', 'PICKED'),
    ('SHIPPED', 'SHIPPED'),
    ('DELIVERED', 'DELIVERED'),
)

class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    tracking_id = models.CharField(max_length=255, blank=False, unique=True)
    status = models.CharField(max_length=50, choices=SHIPMENT_STATUS)
    weight = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    sender = models.CharField(max_length=100, blank=False)
    recipient = models.CharField(max_length=100, blank=False)
    pickup_location = models.TextField()
    target_location = models.TextField()
    date_picked = models.DateTimeField(default=timezone.now)
    value_worth = models.IntegerField(default=0)
    charges = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='shipments')

    def __str__(self) -> str:
        return "%s - %s" %(self.id, self.status)

class ShipmentLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    status = models.CharField(max_length=50, choices=SHIPMENT_STATUS)
    location = models.CharField(max_length=255, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='logs')

    def __str__(self) -> str:
        return "Shipment %s - %s %s" %(self.shipment, self.status, self.created)
