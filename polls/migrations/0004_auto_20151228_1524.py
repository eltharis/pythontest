# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20151228_1257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'choice', 'verbose_name_plural': 'choice|plural'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'question', 'verbose_name_plural': 'question|plural'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choiceText',
            field=models.CharField(max_length=200, verbose_name='choice|choiceText'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='choice|votes'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pubDate',
            field=models.DateTimeField(verbose_name='question|datePublished'),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionText',
            field=models.CharField(max_length=200, verbose_name='question|questionText'),
        ),
    ]