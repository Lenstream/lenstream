from rest_framework import serializers
from rest_framework.reverse import reverse

from channels.models import Channel
from contents.models import Content


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    contents_url = serializers.SerializerMethodField()

    def get_contents_url(self, obj):
        return reverse('channelcontent-list', kwargs={'slug': obj.slug}, request=self.context['request'])

    class Meta:
        model = Channel
        read_only_fields = ('total_users_count', 'active_users_count',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug',},
        }


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        extra_kwargs = {
            'channel': {'lookup_field': 'slug',},
        }
