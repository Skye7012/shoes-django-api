from django.db import models


class Destination(models.Model):
	name = models.CharField(max_length=255)
