# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0008_auto_20170418_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whoarethey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', models.CharField(default='', max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Таблица должностей получателя',
            },
        ),
        migrations.AddField(
            model_name='tableofresources',
            name='test_email',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='postman.Yesno'),
        ),
        migrations.AlterField(
            model_name='tableofresources',
            name='organization_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='postman.Whoarethey'),
        ),
    ]
