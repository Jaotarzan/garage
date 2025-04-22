from django.contrib import admin
from garagem.models import Acessorio, Cor, Modelo, Veiculo

# Register your models here.

admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Modelo)
admin.site.register(Veiculo)