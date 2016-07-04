# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task5_pizza', '0009_auto_20160704_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='date',
            new_name='reg_date',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bonus',
        ),
    ]
