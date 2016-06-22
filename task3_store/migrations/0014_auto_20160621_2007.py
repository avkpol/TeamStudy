# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0013_auto_20160621_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='storeproduct',
            name='productImg',
        ),
        migrations.AddField(
            model_name='storeproduct',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/media/', blank=True),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
