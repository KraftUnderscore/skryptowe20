from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .serializers import \
    CurrencyRatesSerializer, \
    CurrencySummarySerializer
from .models import CurrencyRates, CurrencySummary

# TODO might help with retriving correct objects https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-specific-objects-with-filters

class CurrencyRatesView(ListAPIView):
  serializer_class = CurrencyRatesSerializer
  queryset = CurrencyRates.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['currency', 'date']

class CurrencySummaryView(ListAPIView):
  serializer_class = CurrencySummarySerializer
  queryset = CurrencySummary.objects.all()
