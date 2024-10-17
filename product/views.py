from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from .serializers import AddQuantitySerializer

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from .models import Batch


class ProductCreateView(APIView):
    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)



class AddProductQuantityView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddQuantitySerializer
    lookup_field = 'id'

    @swagger_auto_schema(request_body=AddQuantitySerializer)
    def update(self, request, *args, **kwargs):
        product = self.get_object()  # Get the product instance by ID
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            cost_price = serializer.validated_data['cost_price']
            quantity = serializer.validated_data['quantity']

            # Update the product's quantity
            product.quantity += quantity

           # Create a new batch for tracking
            Batch.objects.create(product=product, quantity=quantity, cost_price=cost_price)

            product.save()  # Save the product instance
            return Response({"message": "Quantity updated successfully."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
