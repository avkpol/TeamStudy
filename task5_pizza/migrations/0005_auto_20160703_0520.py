# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0004_remove_client_ord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
