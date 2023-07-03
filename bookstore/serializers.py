from rest_framework import serializers
from bookstore.models import Book
from category.serializers import CategorySerializer

class BookSerializer(serializers.ModelSerializer):
    """ Book Serializer """
    
    category = CategorySerializer(read_only=True, many=True)
    
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'category',
            'price',
            'image'
        ] 
        
class AddBookSerializer(serializers.ModelSerializer):
    """ Serializer For Adding New Books """
    
    # category = CategorySerializer(read_only=True, many=True)
    
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'author',
            'publisher',
            'isbn',
            'price',
            'category', 
            'price', 
            'image'
        ]
        
class BookDetailSerializer(serializers.Serializer):
    """ Serializer For viewing a Book's Details """
    
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=250)
    author = serializers.CharField(max_length=100)
    publisher = serializers.CharField(max_length=200)
    isbn = serializers.CharField(max_length=13)
    price = serializers.IntegerField()
    category = CategorySerializer(read_only=True, many=True)
    rating = serializers.IntegerField(max_value=5, min_value=1)