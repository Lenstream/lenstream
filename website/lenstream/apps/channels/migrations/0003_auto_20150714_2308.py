# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_auto_20150627_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='active_users_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='channel',
            name='total_users_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
