# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0003_auto_20171113_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='horaF',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horaH',
            field=models.TimeField(),
        ),
    ]
