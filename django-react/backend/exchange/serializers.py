from rest_framework import serializers
from .models import CurrencyRates, CurrencySummary, Orders

class CurrencyRatesSerializer(serializers.ModelSerializer):
  class Meta:
    model = CurrencyRates
    fields = ('currency', 'date', 'mid', 'interpolated')

class CurrencySummarySerializer(serializers.ModelSerializer):
  class Meta:
    model = CurrencySummary
    fields = ('currency', 'date', 'originalSum', 'currencySum')

class OrdersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orders
    fields = ('orderId', 'date', 'amount', 'unitCost')
