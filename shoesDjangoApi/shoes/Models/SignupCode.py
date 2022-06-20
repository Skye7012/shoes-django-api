from django.db import models
from shoes.Models.User import User


class SignupCode(models.Model):
	code = models.EmailField(max_length=255, unique=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
