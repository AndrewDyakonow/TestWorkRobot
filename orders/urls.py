from django.urls import path
from orders.apps import OrdersConfig
from orders.views import create_order

app_name = OrdersConfig.name

urlpatterns = [
    path('', create_order, name='order'),
]
