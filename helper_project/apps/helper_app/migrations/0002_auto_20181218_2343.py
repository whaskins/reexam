# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-18 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='jobs_in_category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='helper_app.Job'),
        ),
    ]
