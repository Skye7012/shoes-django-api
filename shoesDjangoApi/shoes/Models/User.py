from hashlib import sha512

from django.db import models


class User(models.Model):
	email = models.EmailField(max_length=255, unique=True)
	password = models.CharField(max_length=1023)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	phone = models.CharField(max_length=31)
	is_verified = models.BooleanField(default=False)

	@property
	def is_active(self):
		return True

	@property
	def is_authenticated(self):
		return True

	@staticmethod
	def set_password(password):
		return sha512(password.encode()).hexdigest()

	def check_password(self, password):
		return self.password == sha512(password.encode()).hexdigest()
