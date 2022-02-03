from django.http import HttpResponse
from django.template import loader
from xhtml2pdf import pisa

class Courier:
    TEMPLATE_PATH = 'couriers/labels/'
    WAYBILL_TEMPLATE = None
    STATUS_MAP = {}

    def __init__(self, serializer, **kwargs):
        self.WAYBILL_TEMPLATE = self.TEMPLATE_PATH + self.WAYBILL_TEMPLATE
        self.serializer = serializer
    
    def get_shipment_status(self, status):
        return self.STATUS_MAP.get(status, 'Unknown')

    def print_label(self):
        context = {'shipment': self.serializer.data}

        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="waybill.pdf"'

        try:
            # find the template and render it.
            template = loader.get_template(self.WAYBILL_TEMPLATE)
            html = template.render(context)

            # create a pdf
            pisa_status = pisa.CreatePDF(html, dest=response)

        except Exception as e:
            raise RuntimeError("An error occured. Please try again. ", e)

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response

    def cancel_shipment(self, shipment):
        pass

class AramexCourier(Courier):
    WAYBILL_TEMPLATE = 'aramex.html'
    STATUS_MAP = {
        "STILL_NOT_ACCEPTED": "REQUESTED",
        "CANCELLED": "CANCELLED",
        "ACCEPTED": "APPROVED",
        "IN_TRANSIT": "SHIPPED",
        "CUSTOMS_CLEARANCE": "CLEARANCE",
        "DELIVERED": "DELIVERED",
    }

class FedExCourier(Courier):
    WAYBILL_TEMPLATE = 'fedex.html'
    STATUS_MAP = {
        "PROCESSED": "REQUESTED",
        "PICKUP_AVAILABLE": "READ_TO_PICK",
        "ARRIVED": "APPROVED",
        "DEPARTED": "DEPARTED",
        "OUT_FOR_DELIVERY": "DEPARTED",
        "IN_TRANSIT": "SHIPPED",
        "ON_HOLD": "PENDING",
        "CLEARANCE": "CLEARANCE",
        "DELAY": "PENDING",
        "ARRIVED": "DELIVERED",
    }

COURIERS_MAP = {
    "Aramex": AramexCourier,
    "Fedex": FedExCourier
}
