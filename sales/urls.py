from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalesHistoryView.as_view(), name="sales_history"), 
    path('report/', views.SalesReportView.as_view(), name='sales-report'),
    path('sell_product/', views.SellProductView.as_view(), name="sell_product"), 
]