# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_remove_myuser_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bread', models.CharField(max_length=32)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='bread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.Type'),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.MyUser'),
        ),
    ]
