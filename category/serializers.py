from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category Model """
    
    class Meta:
        model = Category 
        fields = ['name']
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    """ Serializer for Detailed view of Category Attributes """
    
    class Meta:
        model = Category 
        fields = ['name', 'description']
