from django.urls import path
from .views import RegistrationApiView, UserAddressApiView, AddressUpdateDestroyApiView, UserPaymentApiView, ShoppingSessionApiView

urlpatterns = [
    path('register/', RegistrationApiView.as_view()),
    path('user_address/', UserAddressApiView.as_view()),
    path('address_edit_or_delete/', AddressUpdateDestroyApiView.as_view()),
    path('user_payment/', UserPaymentApiView.as_view()),
    path('shopping_session/', ShoppingSessionApiView.as_view()),
]