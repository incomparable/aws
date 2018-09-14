# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-29 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(blank=True, max_length=30, null=True)),
                ('series', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(max_length=500)),
                ('pages', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'book',
                'managed': True,
                'verbose_name_plural': 'Book',
            },
        ),
    ]
