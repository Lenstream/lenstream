# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields
import contents.utils


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(0, 'Inactive'), (1, 'Active')])),
                ('activate_date', models.DateTimeField(help_text='keep empty for an immediate activation', null=True, blank=True)),
                ('deactivate_date', models.DateTimeField(help_text='keep empty for indefinite activation', null=True, blank=True)),
                ('content_type', models.PositiveIntegerField(choices=[(0, b'Photo'), (1, b'Video'), (2, b'Text')])),
                ('photo', models.ImageField(max_length=255, upload_to=contents.utils.set_photo_upload_folder, blank=True)),
                ('video', models.FileField(max_length=255, upload_to=contents.utils.set_video_upload_folder, blank=True)),
                ('text', models.CharField(max_length=140, blank=True)),
                ('channel', models.ForeignKey(to='channels.Channel')),
            ],
            options={
                'ordering': ('status', '-activate_date'),
                'abstract': False,
            },
        ),
    ]
