# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0028_auto_20170411_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofsocialnetwork',
            name='name_to_accaunt_page',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='typeofsocialnetwork',
            name='url_to_group_link',
            field=models.CharField(default='', max_length=70),
        ),
    ]
