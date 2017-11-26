# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opencv', '0012_cattle_reg_appliction_req'),
    ]

    operations = [
        migrations.CreateModel(
            name='cattle_face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=20)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.user')),
            ],
        ),
        migrations.AddField(
            model_name='cattle',
            name='fid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='opencv.cattle_face'),
        ),
    ]