# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0007_auto_20160703_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='clt',
            field=models.ForeignKey(default=1, verbose_name=b'Ordered by client', to='task5_pizza.Client'),
            preserve_default=False,
        ),
    ]
