from rest_framework import viewsets
from rest_framework.response import Response

from shoes.Models.Shoe import Shoe
from shoes.Serializers.ShoeSerializer import ShoeSerializer


class ShoeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Shoe.objects.all()
	serializer_class = ShoeSerializer

	def list(self, request, *args, **kwargs):
		items = self.serializer_class(self.queryset, many=True).data
		response = {'count': len(items), 'items': items}
		return Response(response)

