from rest_framework import serializers
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    """ Order Serializer """
    
    customer = serializers.ReadOnlyField()
    cost = serializers.ReadOnlyField(source='get_price')
    
    class Meta:
        model = Order
        fields = ['customer', 'book', 'quantity', 'order_no', 'cost']