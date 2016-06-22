# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent', models.CharField(max_length=50, null=True, verbose_name=b'Trading intermediate', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distributors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distTitle', models.CharField(max_length=50, null=True, verbose_name=b'Distributor', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManufactureProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productName', models.CharField(max_length=255, null=True, verbose_name=b'Product', blank=True)),
                ('manufPrice', models.DecimalField(null=True, verbose_name=b'Manufacturer Price', max_digits=20, decimal_places=2, blank=True)),
                ('manufDate', models.DateField(auto_now_add=True, verbose_name=b'Manufacture Date')),
                ('expDate', models.DateField(auto_now_add=True, verbose_name=b'Expire Date')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=50, null=True, verbose_name=b'Manufacturer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prodCat', models.CharField(max_length=50, verbose_name=b'Product Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=3000, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'product/images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productDesc', models.CharField(max_length=3000, null=True, verbose_name=b'Product Description', blank=True)),
                ('storePrice', models.DecimalField(null=True, verbose_name=b'Store Price', max_digits=20, decimal_places=2, blank=True)),
                ('slug', models.SlugField()),
                ('receiveDate', models.DateField(auto_now_add=True, verbose_name=b'Receive Date')),
                ('inStock', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='task3_store.ProductCategory')),
                ('prodTitle', models.ForeignKey(to='task3_store.ManufactureProduct')),
                ('productImg', models.ForeignKey(to='task3_store.ProductImage')),
            ],
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(to='task3_store.StoreProduct'),
        ),
        migrations.AddField(
            model_name='order',
            name='prodOrdered',
            field=models.ForeignKey(to='task3_store.StoreProduct'),
        ),
    ]
