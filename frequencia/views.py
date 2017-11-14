from django.shortcuts import render
from django.http import HttpResponse
from frequencia.models import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from frequencia.serializers import *
# Create your views here.
class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class ConfiguracoesViewSet(viewsets.ModelViewSet):
    queryset = Configuracoes.objects.all()
    serializer_class = ConfiguracoesSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class JusticativaViewSet(viewsets.ModelViewSet):
    queryset = Justicativa.objects.all()
    serializer_class = JusticativaSerializer