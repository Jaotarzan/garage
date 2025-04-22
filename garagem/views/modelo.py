from rest_framework.viewsets import ModelViewSet

from garagem.models import Modelo

from garagem.serializers.modelo import ModeloSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer