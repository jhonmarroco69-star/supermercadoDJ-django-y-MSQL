from django.urls import path
from .views import (
    ProductoListCreateAPIView,
    ProductoDetailAPIView,
    ClienteListCreateAPIView,
    ClienteDetailAPIView,
    EmpleadoListCreateAPIView,
    EmpleadoDetailAPIView,
    OrdenListCreateAPIView,
    OrdenDetailAPIView
)

urlpatterns = [
    # Rutas de productos
    path('productos/', ProductoListCreateAPIView.as_view(), name='productos'),
    path('productos/<int:pk>/', ProductoDetailAPIView.as_view(), name='producto-detalle'),

    # Rutas de clientes
    path('clientes/', ClienteListCreateAPIView.as_view(), name='clientes'),
    path('clientes/<int:pk>/', ClienteDetailAPIView.as_view(), name='cliente-detalle'),

    # Rutas de empleados
    path('empleados/', EmpleadoListCreateAPIView.as_view(), name='empleados'),
    path('empleados/<int:pk>/', EmpleadoDetailAPIView.as_view(), name='empleado-detalle'),

    # Rutas de órdenes
    path('ordenes/', OrdenListCreateAPIView.as_view(), name='ordenes'),
    path('ordenes/<int:pk>/', OrdenDetailAPIView.as_view(), name='orden-detalle'),
]
