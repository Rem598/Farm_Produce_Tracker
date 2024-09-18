
# Create your models here.
# produce/models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Example: Fruit, Vegetable, Grain
    planting_date = models.DateField()

    def __str__(self):
        return self.name

class Yield(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()  # Yield in kilograms or other units

    def __str__(self):
        return f'{self.crop.name} - {self.amount} kg on {self.date}'

class Sale(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    quantity_sold = models.FloatField()  # Quantity sold in kilograms
    revenue = models.FloatField()  # Revenue from the sale

    def __str__(self):
        return f'Sale of {self.quantity_sold} kg of {self.crop.name} on {self.date}'
