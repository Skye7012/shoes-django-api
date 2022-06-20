from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from shoes.Models.User import User
from shoes.Serializers.UserSerializer import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
				  mixins.UpdateModelMixin,
				  mixins.DestroyModelMixin,
				  GenericViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	# permission_classes = [IsAuthenticated]

	@action(detail=False, methods=['post'])
	def signup(self, request):
		data = request.POST

		try:
			user = User(
				email=data['email'],
				password=data['password'],
				first_name=data['first_name'],
			)
		except MultiValueDictKeyError as e:
			return Response(f"Required field {str(e)} not specified")

		user.last_name = data.get('last_name', '')
		user.phone = data.get('phone', '')

		user.save()
		user_data = self.serializer_class(user).data
		return Response(user_data)
	# serializer = PasswordSerializer(data=request.data)
	# if serializer.is_valid():
	# 	user.set_password(serializer.validated_data['password'])
	# 	user.save()
	# 	return Response({'status': 'password set'})
	# else:
	# 	return Response(serializer.errors,
	# 					status=status.HTTP_400_BAD_REQUEST)

# def retrieve(self, request, *args, **kwargs):
# 	pk = kwargs['pk']
# 	user = User.objects.get(pk=pk)
# 	user = UserSerializer(user).data
# 	return Response(user)
