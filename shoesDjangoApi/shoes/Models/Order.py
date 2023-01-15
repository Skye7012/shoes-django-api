from django.db import models

from shoes.Models.User import User


class Order(models.Model):
	order_date = models.DateField(auto_now_add=True)
	address = models.CharField(max_length=255)
	sum = models.IntegerField()
	count = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
