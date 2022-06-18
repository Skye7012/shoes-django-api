from rest_framework import serializers

from shoes.Models.Shoe import Shoe
from shoes.Serializers.BrandSerializer import BrandSerializer
from shoes.Serializers.DestinationSerializer import DestinationSerializer
from shoes.Serializers.SeasonSerializer import SeasonSerializer


class ShoeSerializer(serializers.ModelSerializer):
	brand = BrandSerializer()
	season = SeasonSerializer()
	destination = DestinationSerializer()

	class Meta:
		model = Shoe
		fields = '__all__'
