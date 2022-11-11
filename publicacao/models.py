from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Publicacao(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_publicacao = models.DateTimeField(default=timezone.now)
    conteudo_publicacao = models.TextField()
    imagem_publicacao = models.ImageField(
        upload_to='media/publicacao/%Y/%m/%d', blank=True, null=True)

    def _str__(self):
        return self.titulo
