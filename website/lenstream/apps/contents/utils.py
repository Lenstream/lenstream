from os.path import abspath, join

from django.conf import settings


def set_photo_upload_folder(instance, filename):
    return abspath(join(settings.MEDIA_ROOT, 'img', instance.channel.slug, filename))


def set_video_upload_folder(instance, filename):
    return abspath(join(settings.MEDIA_ROOT, 'video', instance.channel.slug, filename))
