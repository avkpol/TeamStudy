# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ord',
            field=models.ForeignKey(to='task5_pizza.Order', unique=True),
        ),
    ]
