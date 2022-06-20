import uuid

from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.db import transaction
from django.db.models import Model
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from shoes.Models.SignupCode import SignupCode
from shoes.Models.Token import Token
from shoes.Models.User import User
from shoes.Serializers.UserSerializer import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
				  mixins.UpdateModelMixin,
				  mixins.DestroyModelMixin,
				  GenericViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

	@transaction.atomic
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

		send_signup_email(user)

		user_data = self.serializer_class(user).data
		return Response(user_data)

	@action(detail=False, methods=['post'])
	def login(self, request):
		data = request.POST

		try:
			email = data['email']
			password = data['password']
		except MultiValueDictKeyError as e:
			return Response(f"Required field {str(e)} not specified")

		user = User.objects.get(email=email)

		# if not user.is_verified:
		# 	return Response("User is not verified")
		# elif user.password != password:
		# 	return Response("Wrong password")

		if Token.objects.filter(user=user).exists():
			token = Token.objects.get(user=user)
		else:
			token = Token.objects.create(user=user)

		return Response(f"Token {token.key}")


def send_signup_email(user):
	code = SignupCode(
		code=uuid.uuid4(),
		user=user
	)
	code.save()

	subject = 'Signup verification'
	body = f'Verify your email address by clicking on this link:\n{get_verify_link(code.code)}'
	html_content = render_to_string("signup_email_template.html", {'code': code.code})
	to = [user.email]

	email = EmailMultiAlternatives(subject, body, to=to)
	email.attach_alternative(html_content, "text/html")
	email.send()


def get_verify_link(code):
	return f"http://127.0.0.1:8000/verify/?code={code}"

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
