from rest_framework import routers, serializers, viewsets
# from django_filters import filters
# from url_filter.backends.django import DjangoFilterBackend
# from django_filters.filters import Fil
import rest_framework_filters as filters
from rest_framework_filters.backends import DjangoFilterBackend

from models import Bags, Hopper


class HopperSerializer(serializers.HyperlinkedModelSerializer):
    recorded = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = Hopper
        fields = ('recorded', 'level', 'consumed', 'id')

class HopperViewSet(viewsets.ModelViewSet):
    queryset = Hopper.objects.all().order_by('recorded')
    serializer_class = HopperSerializer


class BagsFilter(filters.FilterSet):
    recorded = filters.AllLookupsFilter(name='recorded')
    purchased = filters.AllLookupsFilter(name='purchased')

    # recorded = filters.AllLookupsFilter(name='recorded')
    class Meta:
        model = Bags
        fields = ['purchased', 'price', 'count', 'recorded']

class BagsSerializer(serializers.HyperlinkedModelSerializer):
    recorded = serializers.DateTimeField(allow_null=True)
    class Meta:
        model = Bags
        fields = ('recorded', 'count', 'purchased', 'price', 'consumed', 'id')

class BagsViewSet(viewsets.ModelViewSet):
    # queryset = Bags.objects.all().order_by('recorded')
    queryset = Bags.objects.all()
    serializer_class = BagsSerializer
    # filter_backends = [DjangoFilterBackend]
    filter_backends = (DjangoFilterBackend,)
    filter_class = BagsFilter

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'hopper', HopperViewSet)
router.register(r'bags', BagsViewSet)
