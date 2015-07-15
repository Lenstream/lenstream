from os.path import abspath, join

from django.conf import settings


def set_photo_upload_folder(instance, filename):
    return join('img', instance.channel.slug, filename)


def set_video_upload_folder(instance, filename):
    return join('video', instance.channel.slug, filename)
