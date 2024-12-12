from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajadore
        fields = '__all__'

class HorarioDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDisponible
        fields = '__all__'

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ciudades
        fields = '__all__'