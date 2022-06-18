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
		self.do_filter_queryset()
		totalCount = Shoe.objects.count()
		items = self.serializer_class(self.queryset, many=True).data
		response = {'totalCount': totalCount, 'items': items}
		return Response(response)

	# Фильтрация
	def do_filter_queryset(self):
		params = self.request.query_params
		search_query = params.get('SearchQuery')
		page = params.get('Page', default='1')
		limit = params.get('Limit')
		order_by = params.get('OrderBy')
		is_ascending = params.get('IsAscending', default="true")
		brand_filters = params.getlist('BrandFilters')
		destination_filters = params.getlist('DestinationFilters')
		season_filters = params.getlist('SeasonFilters')


		# Поиск по наименованию
		if search_query:
			self.queryset = self.queryset.filter(name__contains=search_query)

		# Фильтрация по выбранным брэндам
		if brand_filters:
			brand_filters = [int(b) for b in brand_filters]
			self.queryset = self.queryset.filter(brand_id__in=brand_filters)

		# Фильтрация по выбранным назначениям
		if destination_filters:
			destination_filters = [int(d) for d in destination_filters]
			self.queryset = self.queryset.filter(destination_id__in=destination_filters)

		# Фильтрация по выбранным сезонам
		if season_filters:
			season_filters = [int(s) for s in season_filters]
			self.queryset = self.queryset.filter(season_id__in=season_filters)

		# Сортировка
		if order_by and is_ascending:
			order_by = order_by.lower()
			if is_ascending.lower() == 'true':
				self.queryset = self.queryset.order_by(order_by)
			else:
				self.queryset = self.queryset.order_by('-' + order_by)

		# Пагинация
		if page and limit:
			page = int(page)
			limit = int(limit)
			offset = (page - 1) * limit
			self.queryset = self.queryset[offset:offset + limit]


