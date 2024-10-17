from rest_framework import serializers
from .models import Product, UnitMeasurement


class UnitMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasurement
        fields = ['unit_type', 'quantity', 'price_per_unit']  # Adjust the fields based on your model



class ProductSerializer(serializers.ModelSerializer):
    # Assuming this is a nested serializer or related field
    unit_measurements = UnitMeasurementSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['product_name', 'quantity', 'selling_price', 'cost_price', 'category', 'unit_measurements']

    def create(self, validated_data):
        # Extract the nested fields data (unit_measurements)
        unit_measurements_data = validated_data.pop('unit_measurements')

        # Create the Product instance
        product = Product.objects.create(**validated_data)

        # Now handle the creation of the nested UnitMeasurement entries
        for unit_data in unit_measurements_data:
            UnitMeasurement.objects.create(product=product, **unit_data)

        return product



class AddQuantitySerializer(serializers.Serializer):
    cost_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()

