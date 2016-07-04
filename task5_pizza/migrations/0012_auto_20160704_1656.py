# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0011_remove_delivery_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='address',
        ),
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ManyToManyField(to='task5_pizza.Order'),
        ),
    ]
