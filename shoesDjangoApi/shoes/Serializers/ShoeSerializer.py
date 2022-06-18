from rest_framework import serializers

from shoes.Models.Shoe import Shoe
from shoes.Serializers.BrandSerializer import BrandSerializer
from shoes.Serializers.DestinationSerializer import DestinationSerializer
from shoes.Serializers.SeasonSerializer import SeasonSerializer


class ShoeSerializer(serializers.ModelSerializer):
	brand = BrandSerializer()
	destination = DestinationSerializer()
	season = SeasonSerializer()

	class Meta:
		model = Shoe
		fields = ('id', 'name', 'image', 'price', 'brand', 'destination', 'season')


# class GetShoeSerializer(serializers.Serializer):
# 	count = serializers.IntegerField()
# 	items = serializers.ListField()

# class ShoeSerializer(serializers.Serializer):
# 	# count = ShoeItemSerializer().data.count
# 	items = ShoeItemSerializer(data=Shoe.objects.all()).validated_data
#
# 	# class Meta:
# 	# 	fields = ('items',)
