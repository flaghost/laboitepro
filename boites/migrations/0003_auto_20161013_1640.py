# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0002_auto_20161013_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boite',
            name='api_key',
            field=models.CharField(default=b'45541e0b', max_length=8, verbose_name="Cl\xe9 d'API"),
        ),
    ]