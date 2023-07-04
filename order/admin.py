from django.contrib import admin
from order.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no','book','quantity','status','price']
