# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-10 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0026_problem_rename_name_to_legacy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='legacy_name',
            field=models.CharField(max_length=255, verbose_name='legacy name'),
        ),
    ]
