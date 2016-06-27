# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CltOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('distance', models.PositiveIntegerField()),
                ('payed', models.BooleanField(default=False)),
                ('orderDate', models.DateTimeField(auto_now=True)),
                ('destination', models.CharField(max_length=100)),
                ('client', models.ForeignKey(to='task4_taxi.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(null=True, upload_to=b'img/', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('skype', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.IntegerField(null=True, blank=True)),
                ('fulfOrder', models.ForeignKey(to='task4_taxi.CltOrder')),
            ],
        ),
    ]
