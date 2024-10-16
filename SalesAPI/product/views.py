from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

from .models import Batch

class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetailView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class AddProductQuantityView(APIView):
    def patch(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            quantity = request.data.get('quantity')
            cost_price = request.data.get('cost_price')

            # Create a new batch for tracking
            Batch.objects.create(product=product, quantity=quantity, cost_price=cost_price)

            product.quantity += int(quantity)
            product.save()

            return Response({'message': 'Quantity added successfully'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

