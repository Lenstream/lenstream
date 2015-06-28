# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True),
        ),
    ]
