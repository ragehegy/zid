import pytest

from couriers.serializers import *

@pytest.mark.serializers
@pytest.mark.courier
@pytest.mark.django_db
def test_valid_courier_serializer():
    payload = {
        'name': 'Aramex',
        'url': 'https://www.django-rest-framework.org/'
    }
    serializer = CourierSerializer(data=payload)
    assert serializer.is_valid(raise_exception=True) == True
    serializer.save()
    assert serializer.data['id'] is not None
    return serializer.data['id']

@pytest.mark.serializers
@pytest.mark.courier
@pytest.mark.django_db
def test_valid_shipment_serializer():
    courier_id = test_valid_courier_serializer()
    payload = {
        "courier_id": courier_id,
        "status": "REQUESTED",
        "tracking_id": "abcd",
        "sender": "Mohamed",
        "recipient": "Rageh",
        "pickup_location": "New Cairo, Cairo",
        "target_location": "Old Cairo, Cairo",
        "charges": "10"
    }
    serializer = ShipmentSerializer(data=payload)
    assert serializer.is_valid(raise_exception=True) == True
    serializer.save()
    assert serializer.data['id'] is not None
    assert serializer.data['courier']['id'] == courier_id
    return serializer.data['id']