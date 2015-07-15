from django.conf.urls import include, url

from rest_framework import routers

from .views import ChannelViewSet, ContentViewSet, ChannelContentViewSet, ChannelContentListView


root_router = routers.DefaultRouter()
root_router.register(r'channels', ChannelViewSet)
root_router.register(r'contents', ContentViewSet)
# channel_contents_router = routers.NestedSimpleRouter(root_router, r'channels', lookup='channel_slug')
# channel_contents_router.register(r'channelcontents', ChannelContentViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'lenstream.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(root_router.urls)),
    url(r'^channels/(?P<slug>[^/.]+)/contents/', ChannelContentListView.as_view(), name="channelcontent-list"),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
