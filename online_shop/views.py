from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from online_shop.models import Product, Category, ProductInventory, Discount, PaymentDetail, OrderDetails, OrderItems, CardItem, Cart

from online_shop.serializers import ProductSerializer, CategorySerializer, ProductInventorySerializer, DiscountSerializer, PaymentDetailSerializer, OrderDetailsSerializer, OrderItemsSerializer, CartItemSerializer, CartSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend   

# Create your views here.
class ProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['id', 'name' ]

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

class ProductCreateApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_filters = ['id', 'name']
    
class DetailProductApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductInventoryApiView(ListAPIView):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

class DiscountApiView(ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class PaymentDetailApiView(ListCreateAPIView):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer

class PaymentUpdateRemoveApiView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer

class OrderDetailsApiView(ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    
class OrderItemsApiView(ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

# For test

class Demo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'success': "you authenticated"})

class CartItemApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        print(user)
        return(Response({'success': 'permission working'}))
    
    def update(self, request):
        data = request.data
        cart_item = CardItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return(Response({'success': 'Items updated'}))
    
    def post(self, request):
        data = request.data
        user = request.user
        cart  = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CardItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        user = request.user
        data = request.data
        
        cart_item = CardItem.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user = user, ordered=False).first()
        queryset = CardItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return(Response(serializer.data))