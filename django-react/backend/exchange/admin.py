from django.contrib import admin
from .models import CurrencyRates, CurrencySummary, Orders
#TODO the class might not be needed at all - do I need admin access in the API? Maybe use it to populate database
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
