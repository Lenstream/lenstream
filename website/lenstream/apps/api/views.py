from rest_framework import mixins, viewsets

from .serializers import ChannelSerializer, ContentSerializer

from channels.models import Channel
from contents.models import Content


class ChannelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()


class ContentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
