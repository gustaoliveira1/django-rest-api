from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
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


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def edit_content(request, pk):
    try:
        licao = Licao.objects.get(pk=pk)
    except Licao.DoesNotExist as e:
        return Response({ "error": "No Licao matches the given query." }, status=status.HTTP_404_NOT_FOUND)

    conteudo_html = request.data.get('conteudo_html')
    if not conteudo_html:
        return Response({ "conteudo_html": "This field is required." }, status=status.HTTP_400_BAD_REQUEST)

    licao.conteudo_html = conteudo_html
    licao.save()

    serializer = LicoesSerializer(licao)
    return Response(serializer.data, status=status.HTTP_200_OK)