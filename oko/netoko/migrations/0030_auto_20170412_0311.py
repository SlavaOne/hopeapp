# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0029_auto_20170412_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='name_of_country',
            new_name='name_country',
        ),
    ]
