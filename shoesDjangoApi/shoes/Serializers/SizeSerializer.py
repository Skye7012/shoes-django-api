from rest_framework import serializers

from shoes.Models.Size import Size


class SizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Size
		fields = '__all__'
