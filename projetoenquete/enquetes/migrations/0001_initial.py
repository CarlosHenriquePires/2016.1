# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_opcao', models.CharField(max_length=120, verbose_name='Texto')),
                ('votos', models.IntegerField(default=0, verbose_name='Número de Votos')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_questao', models.CharField(max_length=255, verbose_name='Texto da Questão')),
                ('data_publicacao', models.DateTimeField(verbose_name='Data da Publicação')),
            ],
        ),
        migrations.AddField(
            model_name='opcao',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquetes.Questao', verbose_name='Questão'),
        ),
    ]
