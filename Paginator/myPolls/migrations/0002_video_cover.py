# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPolls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cover',
            field=models.FileField(null=True, upload_to='cover_image'),
        ),
    ]
