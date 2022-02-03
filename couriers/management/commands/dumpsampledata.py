from django.core.management.base import BaseCommand, CommandError
from couriers.models import Courier

class Command(BaseCommand):

    def handle(self, *args, **options):
        objects = []

        data = [
            {
                "name": "Aramex",
                "url": "https://www.aramex.com",
                'shipment_cancellable': True
            },
            {
                "name": "Fedex",
                "url": "https://www.fedex.com",
                'shipment_cancellable': False
            }
        ]
        for courier in data:
            objects.append(Courier(**courier))
        try:
            print("Dumping sample data..")
            Courier.objects.bulk_create(objects)
        except Exception as e:
            raise CommandError("An Error Occured: %s" %e)

        print(f'Stored {len(data)} records.')