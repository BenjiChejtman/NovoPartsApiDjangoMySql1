from django.db import models

class novo(models.Model):
	Part = models.CharField(max_length=150)
	Code = models.CharField(max_length=150)
	Quantity = models.PositiveIntegerField(max_length=150)
	StockAvailableQuantity = models.PositiveIntegerField(max_length=150)
	StockAvailableYesNo = models.CharField(max_length=50)
	Price = models.PositiveIntegerField	(max_length=50)
