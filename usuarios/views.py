from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from usuarios.permissions import IsOwnerOrReadOnly



class UsuarioRegisterView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]


class UsuarioDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsOwnerOrReadOnly]