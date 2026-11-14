
from rest_framework import serializers
from .models import Producto, Cliente, Empleado 
from .models import Producto, Cliente, Empleado, Orden


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'