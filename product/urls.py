from django.urls import path
from . import views 

urlpatterns = [
    path("add_product/", views.ProductCreateView.as_view(), name='add_product'),
    path("<str:id>/", views.ProductDetailView.as_view(), name='product_detail'),
    path("<int:id>/add_quantity/", views.AddProductQuantityView.as_view(), name='add_quantity'),
]