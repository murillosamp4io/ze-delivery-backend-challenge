from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from partner.models import Partner
from .serializers import PartnerSerializer


class GeolocationViewSet(ModelViewSet):
    queryset = Partner.objects.all()

    serializer_class = PartnerSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['address', ]

    def get_queryset(self):
        search = super().get_queryset()
        lat = self.request.query_params.get('lat')
        long = self.request.query_params.get('lng')

        if lat and long:
            point = GEOSGeometry('POINT(' + str(long) + ' ' + str(lat) + ')', srid=4326)
            search = search.annotate(distance=Distance('coverageArea', point)).order_by('coverageArea')

        return search
