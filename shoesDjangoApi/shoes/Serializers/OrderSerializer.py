from rest_framework import serializers

from shoes.Models.Order import Order
from shoes.Serializers.OrderItemSerializer import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
	orderDate = serializers.DateField(source='order_date', required=False)
	sum = serializers.IntegerField(required=False)
	count = serializers.IntegerField(required=False)
	orderItems = OrderItemSerializer(many=True, read_only=True)

	class Meta:
		model = Order
		fields = ['id', 'orderDate', 'address', 'sum', 'count', 'orderItems']
		# exclude = ['order_date']
		read_only_fields = ['id', 'user']
