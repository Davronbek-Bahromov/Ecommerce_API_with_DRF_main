from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserPayment, UserAddress, ShoppingSession

# Register your models here.
admin.site.register(UserAddress)
admin.site.register(ShoppingSession)

admin.site.register(UserPayment)