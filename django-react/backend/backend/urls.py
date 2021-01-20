from django.contrib import admin
from django.urls import path, include
from exchange import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rates/', views.CurrencyRatesView.as_view(), name="rates"),
    path('api/summary/', views.CurrencySummaryView.as_view(), name="summary"),
]
