import pytest

from couriers.models import *

@pytest.mark.models
@pytest.mark.courier
@pytest.mark.django_db
def test_create_courier():
    courier = Courier.objects.create(id="d28861af-00da-4921-9293-345ebbd63521", name="test courier 2")
    assert courier is not None
    return courier

@pytest.mark.models
@pytest.mark.shipment
@pytest.mark.django_db
def test_create_shipment():
    shipment = Shipment.objects.create(courier=test_create_courier(), status='NEW')
    assert shipment is not None
    return shipment

@pytest.mark.models
@pytest.mark.shipment_log
@pytest.mark.django_db
def test_create_log():
    shipment_log = ShipmentLog.objects.create(shipment=test_create_shipment(), status='NEW')
    assert shipment_log is not None
    return shipment_log
