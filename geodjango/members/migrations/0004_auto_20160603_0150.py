# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20160603_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='/media/img/dog.png', upload_to='img/usrpics'),
        ),
    ]