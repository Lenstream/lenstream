from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

class ImageHyperlinkField(serializers.ImageField):

    """
    Custom field which delivers the absolute URI of an image.
    """

    def to_representation(self, value):
        if value:
            try:
                request = self.context.get('request', None)
                return request.build_absolute_uri(value.url)
            except:
                return super(ImageHyperlinkField, self).to_representation(value)
        return ""


# Heavily based on
# https://github.com/dessibelle/sorl-thumbnail-serializer-field/
class ThumbnailImageHyperlinkField(ImageHyperlinkField):

    """
    Custom field which delivers the absolute URI of a sorl-thumbnail for a
    specified image.

    Dimensions are required for this to work properly.  In the event dimensions
    are not supplied, it will rely on ImageHyperlinkField to generate an
    absolute URI to the full-size image.
    """

    def __init__(self, dimensions, options={}, *args, **kwargs):

        self.dimensions = dimensions
        self.options = options

        super(ThumbnailImageHyperlinkField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            image = get_thumbnail(value, self.dimensions, **self.options)
            request = self.context.get('request', None)
            return request.build_absolute_uri(image.url)
        except:
            return super(ThumbnailImageHyperlinkField, self).to_representation(value)
