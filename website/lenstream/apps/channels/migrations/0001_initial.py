# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(0, 'Inactive'), (1, 'Active')])),
                ('activate_date', models.DateTimeField(help_text='keep empty for an immediate activation', null=True, blank=True)),
                ('deactivate_date', models.DateTimeField(help_text='keep empty for indefinite activation', null=True, blank=True)),
                ('total_users_count', models.PositiveIntegerField()),
                ('active_users_count', models.PositiveIntegerField()),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'title', verbose_name='slug', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
            ],
            options={
                'ordering': ('status', '-activate_date'),
                'abstract': False,
            },
        ),
    ]
