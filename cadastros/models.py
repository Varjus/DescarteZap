from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Doadores(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=True)
    sobrenome = models.CharField(max_length=20, blank=False, null=True)
    dataNascimento = models.DateField(max_length=10, blank=False, verbose_name="Data de Nascimento", null=True)
    endereco = models.CharField(max_length=100, blank=False, null=True)
    numero = models.CharField(max_length=10, blank=False, null=True)
    complemento = models.CharField(max_length=10, blank=False, null=True)
    bairro = models.CharField(max_length=20, blank=False, null=True)
    cidade = models.CharField(max_length=20, blank=False, null=True)
    telefonefixo = models.CharField(max_length=20, blank=False, unique=True, verbose_name="Telefone Fixo", null=True)
    celular = models.CharField(max_length=20, blank=False, unique=True, null=True)
    username = models.OneToOneField(User, max_length=20, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.bairro, self.username)


class Doacao(models.Model):
    quantidade = models.FloatField(verbose_name="Quantidade (l)", null=False)
    descricao = models.CharField(max_length=300, null=False, blank=False, verbose_name="Descrição")
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return "{} ({})".format(self.username, self.quantidade)
