from rest_framework import serializers

from shoes.Models.Shoe import Shoe
from shoes.Serializers.BrandSerializer import BrandSerializer
from shoes.Serializers.DestinationSerializer import DestinationSerializer
from shoes.Serializers.SeasonSerializer import SeasonSerializer


class ShoeSerializer(serializers.ModelSerializer):
	brand = BrandSerializer()
	destination = DestinationSerializer()
	season = SeasonSerializer()
	ruSizes = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='ru_size'
	)

	class Meta:
		model = Shoe
		fields = ('id', 'name', 'image', 'price', 'brand', 'destination', 'season', 'ruSizes')


