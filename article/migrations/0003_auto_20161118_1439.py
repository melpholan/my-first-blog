# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20161118_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
