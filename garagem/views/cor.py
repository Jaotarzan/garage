from rest_framework.viewsets import ModelViewSet

from garagem.models import Cor

from garagem.serializers.cor import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer