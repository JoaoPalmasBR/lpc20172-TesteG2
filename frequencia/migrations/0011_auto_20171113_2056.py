# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0010_auto_20171113_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='ipF',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='status',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
