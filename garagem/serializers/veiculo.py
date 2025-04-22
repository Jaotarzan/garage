from rest_framework import serializers

from garagem.models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'modelo', 'cor', 'ano', 'preco', 'acessorios']
        read_only_fields = ('id',)