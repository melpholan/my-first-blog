# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20161118_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]