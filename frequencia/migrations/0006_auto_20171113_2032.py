# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0005_auto_20171113_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='configuracaoFu',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='configuracaoFu',
            field=models.ManyToManyField(null=True, to='frequencia.Configuracoes'),
        ),
    ]
