# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-23 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170923_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='cell',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
