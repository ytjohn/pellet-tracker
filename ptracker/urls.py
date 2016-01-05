from django.conf.urls import url, include
from django.views.generic import RedirectView
import rest_framework_swagger

from ptracker.views import router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/api/')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
