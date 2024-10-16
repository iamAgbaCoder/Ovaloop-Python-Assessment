from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sale
from product.models import Batch, Product

# Create your views here.

class SellProductView(APIView):
    def post(self, request):
        sales_data = request.data.get('sales')
        total_profit = 0

        for sale in sales_data:
            product_id = sale['product_id']
            quantity = sale['quantity']
            unit = sale['unit']

            product = Product.objects.get(id=product_id)
            selling_price = product.unit_measurements.get(unit)

            # FIFO cost price calculation logic
            remaining_quantity = quantity
            total_cost = 0

            batches = Batch.objects.filter(product=product).order_by('created_at')

            for batch in batches:
                if remaining_quantity <= 0:
                    break
                if batch.quantity >= remaining_quantity:
                    total_cost += remaining_quantity * batch.cost_price
                    batch.quantity -= remaining_quantity
                    remaining_quantity = 0
                else:
                    total_cost += batch.quantity * batch.cost_price
                    remaining_quantity -= batch.quantity
                    batch.quantity = 0
                batch.save()

            profit = (selling_price * quantity) - total_cost
            total_profit += profit

            # Save Sale record
            Sale.objects.create(
                product=product, quantity_sold=quantity, unit=unit,
                selling_price=selling_price, profit=profit
            )

        return Response({'total_profit': total_profit}, status=status.HTTP_201_CREATED)



class SalesHistoryView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        sales_data = [{
            'product': sale.product.product_name,
            'quantity_sold': sale.quantity_sold,
            'unit': sale.unit,
            'profit': sale.profit,
            'created_at': sale.created_at
        } for sale in sales]
        return Response(sales_data, status=status.HTTP_200_OK)

