from uuid import uuid4

from django.db import models

SHIPMENT_STATUS = (
    ('NEW', 'NEW'),
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('DELIVERED', 'DELIVERED'),
    ('NOT_DELIVERED', 'NOT_DELIVERED'),
)

class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    status = models.CharField(max_length=50, choices=SHIPMENT_STATUS)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='shipments')

    def __str__(self) -> str:
        return "%s - %s" %(self.id, self.status)

class ShipmentLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    status = models.CharField(max_length=50, choices=SHIPMENT_STATUS)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='logs')

    def __str__(self) -> str:
        return "Shipment %s - %s %s" %(self.shipment, self.status, self.created)

class WayBill(models.Model):
    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE, related_name='waybill', primary_key=True)
