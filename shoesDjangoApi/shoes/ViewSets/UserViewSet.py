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
	def sign_up(self, request):
		data = request.data
		user = User(
			email=data['email'],
			password=data['password'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			phone=data['phone'],
		)
		user.save()
		return Response()
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
