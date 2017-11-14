from django.db import models

# Create your models here.
class Horario (models.Model):
    horaH = models.TimeField()
    def __str__(self):
        return "{}".format(self.horaH)

class Funcionario (models.Model):
    nomeFu = models.CharField(max_length=128)
    emailFu = models.CharField(max_length=128)
    def __str__(self):
        return "{}".format(self.nomeFu)
class Configuracoes (models.Model):
    horarioC = models.ForeignKey(Horario, null=True, blank=False)
    tiposC = (
        (u'ENTRADA MANHA',u'ENTRADA MANHA'), (u'SAIDA MANHA',u'SAIDA MANHA'),
        (u'ENTRADA TARDE',u'ENTRADA TARDE'), (u'SAIDA TARDE',u'SAIDA TARDE'),
    )
    tipoC = models.CharField(max_length=20, choices=tiposC)
    funcionarioC = models.ForeignKey(Funcionario, null=True, blank=False)
    def __str__(self):
        return "{}, {}".format(self.funcionarioC, self.horarioC.__str__)
class Frequencia (models.Model):
    funcionarioF = models.ForeignKey(Funcionario, null=True, blank=False)
    tiposF = (
        (u'ENTRADA',u'ENTRADA'),
        (u'SAIDA',u'SAIDA'),
    )
    tipoF = models.CharField(max_length=7, choices=tiposF)
    horaF = models.TimeField(auto_now=True)
    chefeF = models.ForeignKey(Funcionario, null=True, blank=False, related_name="chefeF")
    ipF = models.CharField(max_length=128,null=True, blank=False)
    status = models.CharField(max_length=128,null=True, blank=False)
    def __str__(self):
        return "{}, {}, {}".format(self.funcionarioF, self.horaF, self.status)
    
class Justicativa (models.Model):
    frequencia = models.ForeignKey(Frequencia, null=True, blank=False)
    justificativa = models.CharField(max_length=256)
    def __str__(self):
        return "{}, {}".format(self.frequencia, self.justificativa)