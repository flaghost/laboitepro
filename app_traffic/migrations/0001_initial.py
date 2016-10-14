# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0006_auto_20161014_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppTraffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activ\xe9e sur votre bo\xeete', verbose_name='App activ\xe9e ?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Derni\xe8re activit\xe9')),
                ('start', models.CharField(default=None, max_length=1024, null=True, verbose_name='Starting Point')),
                ('dest', models.CharField(default=None, max_length=1024, null=True, verbose_name='Destination')),
                ('trajectory_name', models.CharField(default=None, max_length=128, null=True, verbose_name='Itineray Name')),
                ('trip_duration', models.PositiveSmallIntegerField(default=None, max_length=128, null=True, verbose_name='Duration')),
                ('boite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
            options={
                'verbose_name': 'Configuration : traffic',
                'verbose_name_plural': 'Configurations : traffic',
            },
        ),
    ]
