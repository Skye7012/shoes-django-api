from rest_framework import serializers
from shoes.Models.User import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ['password', 'is_verified']
		read_only_fields = ['email']
