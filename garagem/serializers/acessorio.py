from rest_framework import serializers

from garagem.models import Acessorio

class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = ['id', 'descricao']
        read_only_fields = ('id',)