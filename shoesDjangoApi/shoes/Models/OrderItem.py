from django.db import models

from shoes.Models.Order import Order
from shoes.Models.Shoe import Shoe
from shoes.Models.Size import Size


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
