from django.shortcuts import render
from rest_framework import viewsets
from .serializers import \
    CurrencyRatesSerializer, \
    CurrencySummarySerializer, \
    OrdersSerializer
from .models import CurrencyRates, CurrencySummary, Orders

class CurrencyRatesView(viewsets.ModelViewSet):
  serializer_class = CurrencyRatesSerializer
  queryset = CurrencyRates.objects.all()

class CurrencySummaryView(viewsets.ModelViewSet):
  serializer_class = CurrencySummarySerializer
  queryset = CurrencySummary.objects.all()

class OrdersView(viewsets.ModelViewSet):
  serializer_class = OrdersSerializer
  queryset = Orders.objects.all()
