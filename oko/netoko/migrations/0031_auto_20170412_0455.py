# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0030_auto_20170412_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listofcontentgroupofbot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cont_group', models.CharField(default='', max_length=200)),
                ('id_group_in_ss', models.CharField(default='', max_length=20)),
                ('describe', models.CharField(default='', max_length=200)),
                ('type_of_social_net', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='netoko.Typeofsocialnetwork')),
            ],
        ),
        migrations.RemoveField(
            model_name='contentgroupofbot',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='contentgroupofbot',
            name='id_group_in_ss',
        ),
        migrations.RemoveField(
            model_name='contentgroupofbot',
            name='name_cont_group',
        ),
        migrations.RemoveField(
            model_name='contentgroupofbot',
            name='type_of_social_net',
        ),
        migrations.AlterField(
            model_name='contentgroupofbot',
            name='group_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='netoko.Listofcontentgroupofbot'),
        ),
    ]
