from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel

from channels.models import Channel

from .utils import set_photo_upload_folder, set_video_upload_folder


class Content(ActivatorModel, TimeStampedModel):
    CONTENT_TYPE_CHOICES = (
        (0, 'Photo'),
        (1, 'Video'),
        (2, 'Text')
    )

    channel = models.ForeignKey(Channel, limit_choices_to={'status': ActivatorModel.ACTIVE_STATUS})
    content_type = models.PositiveIntegerField(choices=CONTENT_TYPE_CHOICES)
    photo = models.ImageField(upload_to=set_photo_upload_folder, max_length=255, blank=True)
    video = models.FileField(upload_to=set_video_upload_folder, max_length=255, blank=True)
    text = models.CharField(max_length=140, blank=True)
