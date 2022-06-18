from django.db import models

from shoes.models import Brand, Season, Destination


class Shoe(models.Model):
	name = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	price = models.IntegerField()
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
	season = models.ForeignKey(Season, on_delete=models.CASCADE)
