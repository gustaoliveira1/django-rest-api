from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from licoes.models import Licao
from licoes.serializers import LicoesSerializer
from licoes.permissions import IsOwnerOrReadOnly


class LicoesRegisterView(CreateAPIView):
    queryset = Licao.objects.all()
    serializer_class = LicoesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LicoesRetriveView(RetrieveAPIView):
    queryset = Licao.objects.all()
    serializer_class = LicoesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]