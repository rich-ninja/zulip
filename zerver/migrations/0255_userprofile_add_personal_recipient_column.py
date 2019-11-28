# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0254_merge_0209_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='personal_recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zerver.Recipient'),
        ),
    ]
