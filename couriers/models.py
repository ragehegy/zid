from uuid import uuid4

from django.db import models
from django.utils import timezone

class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField()
    shipment_cancellable = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    tracking_id = models.CharField(max_length=255, blank=False, unique=True)
    status = models.CharField(max_length=50)
    weight = models.FloatField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    sender = models.CharField(max_length=100, blank=False)
    recipient = models.CharField(max_length=100, blank=False)
    pickup_location = models.TextField()
    delivery_location = models.TextField()
    current_location = models.TextField()
    date_picked = models.DateTimeField(default=timezone.now)
    value_worth = models.FloatField(default=0)
    charges = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='shipments')

    def __str__(self) -> str:
        return "%s - %s" %(self.id, self.status)

    def cancel(self):
        if self.courier.shipment_cancellable:
            self.status = "CANCELLED"
            self.save()
            return True

        return False    