from rest_framework import viewsets

from shoes.Models.Brand import Brand
from shoes.Serializers.BrandSerializer import BrandSerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer

