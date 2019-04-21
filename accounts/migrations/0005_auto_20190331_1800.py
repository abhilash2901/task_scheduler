# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-31 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190329_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='credential',
            field=models.FileField(default='123', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='email_password',
            field=models.CharField(default='123', max_length=60),
            preserve_default=False,
        ),
    ]