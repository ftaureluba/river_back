from rest_framework import serializers
from .models import (
    JugadorModel
)

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = JugadorModel
        fields = '__all__'

