from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleDescriptionModel
from django_extensions.db.fields import AutoSlugField


class Channel(ActivatorModel, TimeStampedModel, TitleDescriptionModel):
    slug = AutoSlugField(populate_from='title', editable=True, db_index=True)
    total_users_count = models.PositiveIntegerField(default=0)
    active_users_count = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.slug)
