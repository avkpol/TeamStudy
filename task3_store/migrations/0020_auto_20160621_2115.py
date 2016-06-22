# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0019_auto_20160621_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='image',
            field=models.ImageField(null=True, upload_to=b'img/', blank=True),
        ),
    ]
