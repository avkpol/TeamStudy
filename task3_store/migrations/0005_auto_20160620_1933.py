# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0004_auto_20160620_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='description',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/media/images/', blank=True),
        ),
        migrations.AlterField(
            model_name='storeproduct',
            name='productDesc',
            field=models.TextField(max_length=3000, null=True, verbose_name=b'Product Description', blank=True),
        ),
    ]
