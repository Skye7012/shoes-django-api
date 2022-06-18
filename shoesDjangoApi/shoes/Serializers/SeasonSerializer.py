from rest_framework import serializers

from shoes.Models.Season import Season


class SeasonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Season
		fields = '__all__'
