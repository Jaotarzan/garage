from rest_framework import serializers

from garagem.models import Modelo

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['id', 'nome', 'marca']
        read_only_fields = ('id',)