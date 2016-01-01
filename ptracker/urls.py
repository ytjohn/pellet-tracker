from django.conf.urls import url, include
from django.views.generic import RedirectView
from rest_framework import routers, serializers, viewsets

from models import Bags, Hopper

class HopperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hopper
        fields = ('recorded', 'level', 'consumed', 'id')

class HopperViewSet(viewsets.ModelViewSet):
    queryset = Hopper.objects.all().order_by('recorded')
    serializer_class = HopperSerializer

class BagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bags
        fields = ('recorded', 'count', 'purchased', 'price', 'consumed')

class BagsViewSet(viewsets.ModelViewSet):
    queryset = Bags.objects.all().order_by('recorded')
    serializer_class = BagsSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'hopper', HopperViewSet)
router.register(r'bags', BagsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/api/')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
