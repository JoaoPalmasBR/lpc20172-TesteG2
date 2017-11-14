from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from frequencia.models import *

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('url','horaH',)
    def create(self, validated_data):
        horario_data = Horario.objects.create(**validated_data)
        return horario_data
class ConfiguracoesSerializer(serializers.ModelSerializer):
    horarioC = HorarioSerializer()
    class Meta:
        model = Configuracoes
        fields = ('url','horarioC','tipoC','funcionarioC')
    
    def create(self, validated_data):
        horarioCdata = validated_data.pop('horarioC')
        horario1 = Horario.objects.create(**horarioCdata)
        configuracoes = Configuracoes.objects.create(horarioC = horario1, **validated_data)
        return configuracoes
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('url','nomeFu','emailFu')
    
    def create(self, validated_data):
        funcionario = Funcionario.objects.create(**validated_data)
        return funcionario
class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = ('url','funcionarioF','tipoF','horaF','chefeF','ipF')
        read_only_fields = ('status',)    
    def create(self, validated_data):
        frequencia = Frequencia.objects.create(**validated_data)
        return frequencia
class JusticativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Justicativa
        fields = ('url','frequencia','justificativa')
    def create(self, validated_data):
        #frequencia=Frequencia.objects.filter(pk=validated_data.pop('frequencia')
        justicativa = Justicativa.objects.create(**validated_data)
        return justicativa