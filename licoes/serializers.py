from rest_framework import serializers
from licoes.models import Licao


class LicoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licao
        fields = ['id', 'titulo', 'conteudo_html', 'owner']
        read_only_fields = ['id', 'owner']