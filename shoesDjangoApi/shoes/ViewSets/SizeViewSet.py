from rest_framework import viewsets

from shoes.Models.Size import Size
from shoes.Serializers.SizeSerializer import SizeSerializer


class SizeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Size.objects.all()
	serializer_class = SizeSerializer

