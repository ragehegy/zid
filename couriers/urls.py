from django.urls import path

from . import views

urlpatterns = [
    path('couriers/', views.CourierView.as_view({'get': 'list', 'post': 'add_courier'}), name='couriers'),
    path('couriers/<str:pk>/', views.CourierView.as_view({'get': 'retrieve'})),

    path('shipments/', views.ShipmentView.as_view({'get': 'list', 'post': 'add_shipment'}), name='shipments'),
    path('shipments/<str:pk>/', views.ShipmentView.as_view({'get': 'retrieve'})),
    path('shipments/<str:pk>/print/', views.ShipmentView.as_view({'get': 'print_label'})),
    path('shipments/<str:pk>/track/', views.ShipmentView.as_view({'get': 'track_shipment'})),
    path('shipments/<str:pk>/cancel/', views.ShipmentView.as_view({'patch': 'cancel_shipment'})),
]