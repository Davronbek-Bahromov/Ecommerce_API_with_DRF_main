from rest_framework import serializers
from online_shop.models import Product, Category, ProductInventory, Discount, PaymentDetail, OrderDetails, OrderItems, CardItem, Cart

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id', 'quantity', 'created_at']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'description', 'discount_percent', 'active', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'photo1', 'photo2', 'photo3', 'SKU', 'description', 'currency', 'price', 'created_at', ]

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = ['id', 'amount', 'provider', 'status', 'created_at']

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ['user_id', 'total', 'payment_id', 'created_at']

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['order_id', 'product_id', 'quantity', 'created_at']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ['cart', 'user', 'product_id', 'price', 'total_items', 'quantity', 'created_at']
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'ordered', 'total_price']