# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0003_auto_20160626_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='tourists',
        ),
    ]
