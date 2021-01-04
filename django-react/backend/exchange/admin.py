from django.contrib import admin
from .models import CurrencyRates, CurrencySummary, Orders

# Register your models here.
class CurrencyRatesAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'mid', 'interpolated')

class CurrencySummaryAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'originalSum', 'currencySum')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('orderId', 'date', 'amount', 'unitCost')

admin.site.register(CurrencyRates, CurrencyRatesAdmin)
admin.site.register(CurrencySummary, CurrencySummaryAdmin)
admin.site.register(Orders, OrdersAdmin)
