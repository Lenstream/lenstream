from rest_framework import serializers

from channels.models import Channel
from contents.models import Content


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        read_only_fields = ('total_users_count', 'active_users_count',)


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
