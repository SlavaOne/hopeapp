# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0027_auto_20170410_0758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botinfosindiffrentsocnet',
            old_name='login',
            new_name='password',
        ),
        migrations.AddField(
            model_name='botinfosindiffrentsocnet',
            name='id_in_ss',
            field=models.CharField(default='', max_length=30),
        ),
    ]
