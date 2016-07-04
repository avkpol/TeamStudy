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
                ('last_name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('phone', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_children', models.BooleanField(default=False)),
                ('bonus', models.IntegerField(default=2, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientChild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=255, choices=[(b'boy', b'boy'), (b'girl', b'girl')])),
                ('photo', models.ImageField(null=True, upload_to=b'img/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(null=True, upload_to=b'img/', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('skype', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payed', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('orderDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('discount_price', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('payed', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('orderDate', models.DateTimeField(auto_now=True)),
                ('clt', models.ForeignKey(verbose_name=b'Ordered by client', to='task5_pizza.Client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['address'],
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pizza_title', models.CharField(max_length=50)),
                ('pizza_size', models.CharField(max_length=50, choices=[(b'mini', b'mini'), (b'normal', b'normal'), (b'normal', b'giant')])),
                ('pizza_title_price', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.ForeignKey(to='task5_pizza.Pizza'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='address',
            field=models.ManyToManyField(to='task5_pizza.OrderAddress'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='client',
            field=models.ForeignKey(to='task5_pizza.Client'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='courier',
            field=models.ManyToManyField(to='task5_pizza.Courier'),
        ),
        migrations.AddField(
            model_name='courier',
            name='fulf_order',
            field=models.ForeignKey(to='task5_pizza.Order'),
        ),
        migrations.AddField(
            model_name='client',
            name='child',
            field=models.ForeignKey(to='task5_pizza.ClientChild'),
        ),
        migrations.AddField(
            model_name='client',
            name='ord',
            field=models.OneToOneField(to='task5_pizza.Order'),
        ),
    ]
