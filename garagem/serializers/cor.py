from rest_framework import serializers

from garagem.models import Cor

class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = ['id', 'nome']
        read_only_fields = ('id',)