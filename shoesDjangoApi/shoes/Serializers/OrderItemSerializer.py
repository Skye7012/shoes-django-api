from rest_framework import serializers

from shoes.Models.OrderItem import OrderItem
from shoes.Serializers.ShoeSerializer import SimpleShoeSerializer


class OrderItemSerializer(serializers.ModelSerializer):
	ruSize = serializers.IntegerField(source='size.ru_size')
	shoe = SimpleShoeSerializer()

	class Meta:
		model = OrderItem
		fields = ['id', 'ruSize', 'shoe']
		# exclude = ['size']
		# read_only_fields = ['id', 'ruSize', 'shoe']
