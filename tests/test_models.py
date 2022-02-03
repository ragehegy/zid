import pytest

from couriers.models import *

@pytest.mark.models
@pytest.mark.courier
@pytest.mark.django_db
def test_create_courier():
    data = {
        "name": "test",
        "url": "https://www.django-rest-framework.org/api-guide/viewsets/",
        'shipment_cancellable': False
    }
    courier = Courier.objects.create(id="d28861af-00da-4921-9293-345ebbd63521", name="test courier 2")
    assert courier is not None
    return courier

@pytest.mark.models
@pytest.mark.shipment
@pytest.mark.django_db
def test_create_shipment():
    data = {
        'courier': test_create_courier(),
        "status": "REQUESTED",
        "tracking_id": "abcd",
        "sender": "Mohamed",
        "recipient": "Rageh",
        "charges": "10"
    }
    shipment = Shipment.objects.create(**data)
    assert shipment is not None
    return shipment
    
@pytest.mark.models
@pytest.mark.shipment
@pytest.mark.django_db
def test_cancel_shipment():
    shipment = test_create_shipment()
    assert shipment is not None
    assert shipment.cancel() is not True
    