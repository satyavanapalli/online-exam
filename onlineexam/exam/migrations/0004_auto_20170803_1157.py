# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-03 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20170718_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='duration',
            field=models.DurationField(default=1200),
        ),
    ]