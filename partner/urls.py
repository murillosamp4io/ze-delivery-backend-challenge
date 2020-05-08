from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from partner.geolocation.viewsets import GeolocationViewSet

actions = {
    'get': 'list',
    'post': 'create'
}

retrieve_action = {
    'get': 'retrieve',
}

router = routers.DefaultRouter()
router.register(r'partner', GeolocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('partner/', GeolocationViewSet.as_view(actions), name='transactions'),
    path('partner/<pk>', GeolocationViewSet.as_view(retrieve_action), name='transaction'),
]
