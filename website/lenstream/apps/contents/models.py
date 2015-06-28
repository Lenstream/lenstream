from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel

from channels.models import Channel

from .utils import set_photo_upload_folder, set_video_upload_folder


class Content(ActivatorModel, TimeStampedModel):
    CONTENT_TYPE_PHOTO = 0
    CONTENT_TYPE_VIDEO = 1
    CONTENT_TYPE_TEXT = 2
    CONTENT_TYPE_CHOICES = (
        (CONTENT_TYPE_PHOTO, 'Photo'),
        (CONTENT_TYPE_VIDEO, 'Video'),
        (CONTENT_TYPE_TEXT, 'Text')
    )

    channel = models.ForeignKey(Channel, limit_choices_to={'status': ActivatorModel.ACTIVE_STATUS})
    content_type = models.PositiveIntegerField(choices=CONTENT_TYPE_CHOICES, default=CONTENT_TYPE_PHOTO)
    photo = models.ImageField(upload_to=set_photo_upload_folder, max_length=255, blank=True)
    video = models.FileField(upload_to=set_video_upload_folder, max_length=255, blank=True)
    text = models.CharField(max_length=140, blank=True)
