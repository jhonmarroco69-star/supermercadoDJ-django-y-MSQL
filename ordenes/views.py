
from rest_framework import generics
from .models import Producto, Cliente, Empleado
from .serializers import ProductoSerializer, ClienteSerializer, EmpleadoSerializer,OrdenSerializer
from .serializers import (
    ProductoSerializer,
    ClienteSerializer,
    EmpleadoSerializer,
    OrdenSerializer
)
from .models import Producto, Cliente, Empleado, Orden

# Vistas de productos

class ProductoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# Vistas de clientes

class ClienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# Vistas de empleados

class EmpleadoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class EmpleadoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

# Órdenes
class OrdenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Orden.objects.select_related(
        'cliente', 'producto', 'empleado'
    ).all()
    serializer_class = OrdenSerializer


class OrdenDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.select_related(
        'cliente', 'producto', 'empleado'
    ).all()
    serializer_class = OrdenSerializer
