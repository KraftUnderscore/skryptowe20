from django.db import models

# Create your models here.
class CurrencyRates(models.Model):
    currency = models.CharField(max_length=3)
    date = models.CharField(max_length=10)
    mid = models.FloatField()
    interpolated = models.BooleanField()

    def __str__(self):
        return f"Rates for {self.currency} on {self.date} is {self.mid}, interpolated: {self.interpolated}"

class CurrencySummary(models.Model):
    currency = models.CharField(max_length=3)
    date = models.CharField(max_length=10)
    originalSum = models.FloatField()
    currencySum = models.FloatField()

    def __str__(self):
        return f"Sales for {self.currency} on {self.date} is {self.currencySum}, in PLN: {self.originalSum}"

class Orders(models.Model):
    orderId = models.IntegerField()
    date = models.CharField(max_length=10)
    amount = models.IntegerField()
    unitCost = models.FloatField()

    def __str__(self):
        return f"Order {self.orderId} on {self.date} is {self.amount} items for {self.unitCost} PLN"
