# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0009_historypublishtobotandgroupsfromsiteandgroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchopengroupinvK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_group', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
