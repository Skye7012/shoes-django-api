from rest_framework import serializers

from shoes.Models.Destination import Destination


class DestinationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Destination
		fields = '__all__'
