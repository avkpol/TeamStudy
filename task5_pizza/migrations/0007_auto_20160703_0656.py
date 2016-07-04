# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0006_remove_order_clt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderDate',
            new_name='order_date',
        ),
    ]
