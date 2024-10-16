from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer


class UsuarioRegisterView(CreateAPIView):
    queryset = Usuario
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]