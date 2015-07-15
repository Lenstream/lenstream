# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.PositiveIntegerField(default=0, choices=[(0, b'Photo'), (1, b'Video'), (2, b'Text')]),
        ),
    ]
