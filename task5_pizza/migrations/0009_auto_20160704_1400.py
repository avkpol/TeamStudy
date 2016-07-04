# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0008_order_clt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizza_title_price',
        ),
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ManyToManyField(to='task5_pizza.Order'),
        ),
    ]
