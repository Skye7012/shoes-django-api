from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class MyUser(EmailAbstractUser):
	# Custom fields
	phone = models.CharField(max_length=32)

	# Required
	objects = EmailUserManager()
