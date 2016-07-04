# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0002_auto_20160702_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ord',
            field=models.ForeignKey(related_name='+', to='task5_pizza.Order'),
        ),
    ]
