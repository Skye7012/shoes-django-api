from rest_framework import viewsets

from shoes.Models.Destination import Destination
from shoes.Serializers.DestinationSerializer import DestinationSerializer


class DestinationViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Destination.objects.all()
	serializer_class = DestinationSerializer

