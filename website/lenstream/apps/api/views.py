from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import APIException, NotFound

from .serializers import ChannelSerializer, ContentSerializer

from channels.models import Channel
from contents.models import Content


class ChannelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ChannelSerializer
    lookup_field = 'slug'
    queryset = Channel.objects.all()


class ContentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()


class ChannelContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get_queryset(self):
        import pdb; pdb.set_trace()
        # @TODO Get queryset based on channel lookup_field
        return super(ChannelContentViewSet, self).get_queryset()

class ChannelContentListView(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        try:
            slug = self.kwargs['slug']

            if not Channel.objects.filter(slug=slug).exists():
                raise NotFound(detail="Channel with slug '%s' does not exist." % slug)

        except KeyError:
            raise APIException(status_code=400, default_detail="Channel slug not found in the URL")

        return Content.objects.filter(channel__slug=slug)
