from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import ChannelViewSet, ContentViewSet


router = routers.DefaultRouter()
router.register('channels', ChannelViewSet)
router.register('contents', ContentViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lenstream.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
