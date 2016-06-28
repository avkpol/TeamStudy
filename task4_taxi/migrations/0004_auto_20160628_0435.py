# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0003_auto_20160628_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
