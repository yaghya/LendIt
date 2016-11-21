# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-21 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_lendituser_small_pic_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendituser',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='lendituser',
            name='long',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
    ]
