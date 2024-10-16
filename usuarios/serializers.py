from rest_framework import serializers
from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "senha", "data_de_nascimento"]

    def create(self, validated_data):
        senha = validated_data.pop("senha")
        usuario = Usuario(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario