from rest_framework import serializers
from shoes.Models.User import User


class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField()

	class Meta:
		model = User
		exclude = ['password', 'is_verified']
