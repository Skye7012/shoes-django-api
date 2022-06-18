from django.db import models


class Season(models.Model):
	name = models.CharField(max_length=255)
