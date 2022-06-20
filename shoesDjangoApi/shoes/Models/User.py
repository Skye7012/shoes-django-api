from django.db import models


class User(models.Model):
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=1023)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	phone = models.CharField(max_length=31)
	is_verified = models.BooleanField(default=False)
