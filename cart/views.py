from bookstore.models import Book
from cart.models import Cart
from cart.serializers import CartSerializer
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

User = get_user_model()

# Fetching & Adding New Cart Operation
@swagger_auto_schema(method='GET', operation_summary='fetch all cart items')
@swagger_auto_schema(method='POST', operation_summary='add item to cart', request_body=CartSerializer())
@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated]) 
def cart(request):
    """ Fetching & Adding New Cart Operation """
    
    user = request.user
    
    if user.is_anonymous:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == 'GET':
        cart_obj = Cart.objects.filter(user=request.user)
        serializer_class = CartSerializer(cart_obj, many=True)
        context = {
            'status': 'True',
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        book_title = request.data["book"]
        book_obj = Book.objects.get(title=book_title)
        if book_obj:
            serializer_class = CartSerializer(data=request.data)
            if serializer_class.is_valid():
                if 'user' in serializer_class.validated_data.keys():
                    serializer_class.validated_data.pop('user')
                
                cart = Cart.objects.create(**serializer_class.validated_data, user=request.user)
                serializer = CartSerializer(cart)
                context = {
                    'status': True,
                    'message': 'Success',
                    'data': serializer.data
                }
                return Response(context, status=status.HTTP_201_CREATED)
            else:
                context = {
                    'status': False,
                    'error': serializer_class.errors
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

# Modifying Cart Operations    
@swagger_auto_schema(method='GET', operation_summary='fetch cart item by id')
@swagger_auto_schema(method='PUT', operation_summary='modify cart', request_body=CartSerializer())
@swagger_auto_schema(method='DELETE', operation_summary='delete cart item', request_body=CartSerializer())
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def fetch_cartitem_by_id(request, cart_id):
    """ Modifying Cart Operations """
    
    user = request.user
    
    if user.is_anonymous:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        context = {
            'status'  : False,
            'message' : 'Empty Cart'
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers_class = CartSerializer(cart)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializers_class.data
        }
        return Response(context, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializers_class = CartSerializer(cart, data=request.data, partial=True)
        if serializers_class.is_valid():
            serializers_class.save()
            context = {
                'status': True,
                'message': 'Success',
                'data': serializers_class.data
            }
            return Response(context, status=status.HTTP_202_ACCEPTED)
        else:
            context = {
                'status': False,
                'message': 'Failed',
                'error': serializers_class.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cart.delete()
        context = {
            'status'  : True,
            'message' : 'Deleted Successfully'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)
