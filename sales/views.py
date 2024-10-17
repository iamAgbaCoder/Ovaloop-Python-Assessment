from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from sales.serializers import SellProductSerializer
from product.serializers import ProductSerializer
from .models import Sale
from product.models import Batch, Product

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

# Create your views here.

# class SellProductView(APIView):
#     @swagger_auto_schema(method='post', request_body=SellProductSerializer)
#     @api_view(['POST'])
#     def post(self, request):
#         sales_data = request.data.get('sales')
#         total_profit = 0

#         for sale in sales_data:
#             product_id = sale['product_id']
#             quantity = sale['quantity']
#             unit = sale['unit']

#             product = Product.objects.get(id=product_id)
#             selling_price = product.unit_measurements.get(unit)

#             # FIFO cost price calculation logic
#             remaining_quantity = quantity
#             total_cost = 0

#             batches = Batch.objects.filter(product=product).order_by('created_at')

#             for batch in batches:
#                 if remaining_quantity <= 0:
#                     break
#                 if batch.quantity >= remaining_quantity:
#                     total_cost += remaining_quantity * batch.cost_price
#                     batch.quantity -= remaining_quantity
#                     remaining_quantity = 0
#                 else:
#                     total_cost += batch.quantity * batch.cost_price
#                     remaining_quantity -= batch.quantity
#                     batch.quantity = 0
#                 batch.save()

#             profit = (selling_price * quantity) - total_cost
#             total_profit += profit

#             # Save Sale record
#             Sale.objects.create(
#                 product=product, quantity_sold=quantity, unit=unit,
#                 selling_price=selling_price, profit=profit
#             )

#         return Response({'total_profit': total_profit}, status=status.HTTP_201_CREATED)
    




class SellProductView(generics.CreateAPIView):
    serializer_class = SellProductSerializer

    @swagger_auto_schema(request_body=SellProductSerializer)
    # @api_view(['POST'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity_to_sell = serializer.validated_data['quantity']
            unit_measurement = serializer.validated_data['unit_measurement']

            product = Product.objects.get(id=product_id)

            if product.quantity < quantity_to_sell:
                return Response({"error": "Not enough stock available."}, status=status.HTTP_400_BAD_REQUEST)

            total_profit = 0
            quantity_remaining = quantity_to_sell

            # Fetch batches in FIFO order (oldest first)
            batches = product.batches.order_by('created_at')

            for batch in batches:
                if quantity_remaining <= 0:
                    break

                if batch.quantity > 0:
                    if batch.quantity >= quantity_remaining:
                        profit_per_item = product.selling_price - batch.cost_price
                        total_profit += profit_per_item * quantity_remaining

                        batch.quantity -= quantity_remaining
                        batch.save()

                        quantity_remaining = 0
                    else:
                        profit_per_item = product.selling_price - batch.cost_price
                        total_profit += profit_per_item * batch.quantity

                        quantity_remaining -= batch.quantity
                        batch.quantity = 0
                        batch.save()

            # Record the sale
            Sale.objects.create(
                product=product,
                quantity_sold=quantity_to_sell,
                selling_price=product.selling_price,
                profit=total_profit
            )

            # Update the product quantity
            product.quantity -= quantity_to_sell
            product.save()

            return Response({"message": "Product sold successfully.", "total_profit": total_profit}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





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
    



class SalesReportView(APIView):
    def get(self, request, *args, **kwargs):
        sales = Sale.objects.all()  # Retrieve all sales, can filter based on requirements
        total_sales = sales.count()
        total_profit = sum(sale.profit for sale in sales)  # Assuming each sale has a profit field
        
        report = {
            "total_sales": total_sales,
            "total_profit": total_profit,
            "sales_details": [{"id": sale.id, "product": sale.product.product_name, "quantity": sale.quantity_sold, "profit": sale.profit} for sale in sales]
        }

        return Response(report)

