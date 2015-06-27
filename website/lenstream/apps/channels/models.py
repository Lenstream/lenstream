from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel


class Channel(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel):
    total_users_count = models.PositiveIntegerField()
    active_users_count = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s' % self.name
