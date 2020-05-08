from rest_framework.serializers import ModelSerializer

from partner.models import Partner


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'tradingName', 'ownerName', 'document', 'coverageArea', 'address']
