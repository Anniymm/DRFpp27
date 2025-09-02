from rest_framework import serializers
from .models import Product, ProductLog

class ProductLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLog
        # fields = '__all__'
        fields = ['id', 'product', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    # validaciebistvis
    confirm_price = serializers.DecimalField(max_digits=6, decimal_places=2, write_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'in_stock', 'user']
        read_only_fields = ['id']

    def validate(self, data):
        if 'confirm_price' in data and data['price'] != data['confirm_price']:
            raise serializers.ValidationError('price and confirm price does not match')
        return data


