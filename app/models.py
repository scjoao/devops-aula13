"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)

    
class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=13)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=200)

