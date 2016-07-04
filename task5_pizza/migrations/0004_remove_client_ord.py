# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0003_auto_20160702_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='ord',
        ),
    ]
