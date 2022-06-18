from rest_framework import viewsets

from shoes.Models.Season import Season
from shoes.Serializers.SeasonSerializer import SeasonSerializer


class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Season.objects.all()
	serializer_class = SeasonSerializer

