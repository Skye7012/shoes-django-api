from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import rest_framework.status as StatusCodes

from shoes.Models.Shoe import Shoe
from shoes.Serializers.ShoeSerializer import ShoeSerializer


class ShoeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Shoe.objects.all()
	querysetCount = None
	serializer_class = ShoeSerializer

	def list(self, request, *args, **kwargs):
		self.do_filter_queryset()
		total_count = self.querysetCount
		items = self.serializer_class(self.queryset, many=True).data
		response = {'totalCount': total_count, 'items': items}
		return Response(response)

	@action(detail=False, methods=['get'])
	def get_by_ids(self, request):
		ids = request.query_params.getlist('ids')

		if ids is None:
			return Response('Не переданы идентификаторы', status=StatusCodes.HTTP_400_BAD_REQUEST)

		query = self.queryset.filter(id__in=ids)
		items = self.serializer_class(query, many=True).data
		response = {'totalCount': len(items), 'items': items}
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
		size_filters = params.getlist('SizeFilters')


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
			season_filters = [int(d) for d in season_filters]
			self.queryset = self.queryset.filter(season_id__in=season_filters)

		# Фильтрация по выбранным размерам
		if size_filters:
			size_filters = [int(s) for s in size_filters]
			self.queryset = self.queryset.filter(ruSizes__ru_size__in=size_filters).distinct()

		# Сортировка
		if order_by and is_ascending:
			order_by = order_by.lower()
			if is_ascending.lower() == 'true':
				self.queryset = self.queryset.order_by(order_by)
			else:
				self.queryset = self.queryset.order_by('-' + order_by)

		# Кол-во сущностей, прошедших фильтрацию
		self.querysetCount = self.queryset.count()

		# Пагинация
		if page and limit:
			page = int(page)
			limit = int(limit)
			offset = (page - 1) * limit
			self.queryset = self.queryset[offset:offset + limit]


