from django.db.models.functions import Lower
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

	# Фильтрация
	def filter_queryset(self):
		params = self.request.query_params
		search_query = params.get('searchQuery')
		page = params.get('page', default='1')
		limit = params.get('limit')
		order_by = params.get('orderBy')
		is_ascending = params.get('isAscending', default=True)

		# Поиск по наименованию
		if search_query:
			self.queryset = self.queryset.filter(name__contains=search_query)

		# Пагинация
		if page and limit:
			page = int(page)
			limit = int(limit)
			offset = (page - 1) * limit
			self.queryset = self.queryset[offset:offset + limit]

		if order_by and is_ascending:
			if Lower(is_ascending) == 'true':
				self.queryset = self.queryset.order_by(order_by)
			else:
				self.queryset = self.queryset.order_by('-' + order_by)


