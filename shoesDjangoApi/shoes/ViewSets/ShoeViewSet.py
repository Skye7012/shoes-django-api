from rest_framework import viewsets
from rest_framework.response import Response
import django

from shoes.Models.Shoe import Shoe
from shoes.Serializers.ShoeSerializer import ShoeSerializer


class ShoeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Shoe.objects.all()
	serializer_class = ShoeSerializer

	def list(self, request, *args, **kwargs):
		self.filter_queryset()
		items = self.serializer_class(self.queryset, many=True).data
		response = {'count': len(items), 'items': items}
		return Response(response)

	def filter_queryset(self):
		params = self.request.query_params
		search_query = params.get('searchQuery')
		page = int(params.get('page'))
		limit = int(params.get('limit'))

		if search_query:
			self.queryset = self.queryset.filter(name__contains=search_query)

		if page and limit:
			offset = (page-1)*limit
			# self.queryset = self.queryset[(page-1)*limit:limit]
			self.queryset = self.queryset[offset:offset + limit]
