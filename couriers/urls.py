from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourierView.as_view({'get': 'list', 'post': 'add_courier'}), name='couriers'),
    path('<str:pk>/', views.CourierView.as_view({'get': 'retrieve'})),

    path('<str:pk>/shipments/', views.ShipmentView.as_view({'get': 'list', 'post': 'add_shipment'}), name='shipments'),
    path('<str:pk>/', views.ShipmentView.as_view({'get': 'retrieve'})),
]