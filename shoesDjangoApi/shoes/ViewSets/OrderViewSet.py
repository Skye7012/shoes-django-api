from functools import reduce

import rest_framework.status as StatusCodes
from django.db import transaction
from rest_framework import viewsets, mixins, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shoes.Models.Order import Order
from shoes.Models.OrderItem import OrderItem
from shoes.Models.Shoe import Shoe
from shoes.Models.Size import Size
from shoes.Serializers.OrderItemSerializer import OrderItemSerializer
from shoes.Serializers.OrderSerializer import OrderSerializer
from shoes.authentication import TokenAuthentication


class OrderViewSet(mixins.CreateModelMixin,
				   mixins.ListModelMixin,
				   viewsets.GenericViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

	def list(self, request, *args, **kwargs):
		query = Order.objects.filter(user=request.user)
		data = self.serializer_class(query, many=True).data
		for order in data:
			order['orderItems'] = get_order_items(pk=order['id'])

		response = {'totalCount': len(data), 'items': data}
		return Response(response)

	@transaction.atomic
	def create(self, request, *args, **kwargs):
		data = request.data

		address = data.get('address')
		req_order_items = data.get('orderItems')

		order_items = list(map(
			lambda x: OrderItem(
				shoe=Shoe.objects.get(pk=x.get('shoeId')),
				size=Size.objects.get(ru_size=x.get('ruSize'))
			),
			req_order_items
		))

		order = Order.objects.create(
			user=request.user,
			address=address,
			sum=sum(c.shoe.price for c in order_items),
			count=len(order_items),
		)
		order.orderitem_set.add(*order_items, bulk=False)

		order.save()

		response = self.serializer_class(Order.objects.get(pk=order.pk)).data
		response['orderItems'] = get_order_items(response['id'])

		return Response(response, status=StatusCodes.HTTP_201_CREATED)


def get_order_items(pk):
	query = OrderItem.objects.filter(order_id=pk)
	data = OrderItemSerializer(query, many=True).data
	return data
