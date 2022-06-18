from rest_framework import serializers

from shoes.Models.Brand import Brand


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = ('id', 'name')
