from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalesHistoryView.as_view(), name="sales_history"), 
    path('sell_product/', views.SellProductView.as_view(), name="sell_product"), 
]