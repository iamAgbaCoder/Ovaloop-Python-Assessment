from rest_framework import serializers

class SellProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    unit_measurement = serializers.CharField()
