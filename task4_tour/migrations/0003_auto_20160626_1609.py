# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0002_auto_20160626_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='highSn',
        ),
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='lastMinute',
        ),
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='lowSn',
        ),
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='middleSn',
        ),
        migrations.AddField(
            model_name='pricetourcategory',
            name='tourSeason',
            field=models.CharField(default=b'high season', max_length=255, null=True, blank=True),
        ),
    ]
