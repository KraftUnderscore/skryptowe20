from django.shortcuts import render
from rest_framework import viewsets
from .serializers import \
    CurrencyRatesSerializer, \
    CurrencySummarySerializer, \
    OrdersSerializer
from .models import CurrencyRates, CurrencySummary, Orders

# TODO The Views allow for CRUD operations on data, make it GET only.
# TODO might help with retriving correct objects https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-specific-objects-with-filters

class CurrencyRatesView(viewsets.ModelViewSet):
  serializer_class = CurrencyRatesSerializer
  queryset = CurrencyRates.objects.all()

class CurrencySummaryView(viewsets.ModelViewSet):
  serializer_class = CurrencySummarySerializer
  queryset = CurrencySummary.objects.all()

class OrdersView(viewsets.ModelViewSet):
  serializer_class = OrdersSerializer
  queryset = Orders.objects.all()
