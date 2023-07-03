from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    """ Cart Serializer """
    
    class Meta:
        model = Cart
        fields = ['id', 'book', 'created_at']