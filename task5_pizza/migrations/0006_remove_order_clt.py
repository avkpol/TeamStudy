# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0005_auto_20160703_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='clt',
        ),
    ]
