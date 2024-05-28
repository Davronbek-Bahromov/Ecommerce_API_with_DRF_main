from django.urls import path, include
from .views import DetailProductApiView, ProductInventoryApiView, DiscountApiView, PaymentDetailApiView, OrderDetailsApiView, OrderItemsApiView, OrderItemsViewSet, CartItemApiView, ProductApiView, ProductCreateApiView, CategoryApiView, Demo, PaymentUpdateRemoveApiView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("OrderItems", OrderItemsViewSet, basename="orderitems")

urlpatterns = [
    path('', ProductApiView.as_view()),
    # path('demo/', Demo.as_view()),
    path('category/', CategoryApiView.as_view()),
    path('detail/<int:pk>', DetailProductApiView.as_view()),
    path('inventory/', ProductInventoryApiView.as_view()),
    path('discounts/', DiscountApiView.as_view()),
    path('payments/', PaymentDetailApiView.as_view()),
    path('order_detail/', OrderDetailsApiView.as_view()),
    path('AddProduct/', ProductCreateApiView.as_view()),
    path('order_items/', OrderItemsApiView.as_view()),
    path('cart_item/', CartItemApiView.as_view(), name="cart_item"),
    path('payment_edit_or_remove/<int:pk>', PaymentUpdateRemoveApiView.as_view()),
    path('order_items/', include(router.urls))
]