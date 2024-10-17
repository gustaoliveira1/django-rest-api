from django.db import models
from usuarios.models import Usuario


class Licao(models.Model):
    owner = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="licoes")
    titulo = models.CharField(max_length=255)
    conteudo_html = models.TextField()