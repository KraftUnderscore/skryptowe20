from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from exchange import views

router = routers.DefaultRouter()
router.register(r'rates', views.CurrencyRatesView, 'rates')
router.register(r'summary', views.CurrencySummaryView, 'summary')
router.register(r'orders', views.OrdersView, 'orders') # TODO delete after testing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
