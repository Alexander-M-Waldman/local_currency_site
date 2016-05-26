# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 18:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]