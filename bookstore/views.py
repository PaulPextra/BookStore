from bookstore.models import Author, Book
from bookstore.serializers import BookSerializer, BookDetailSerializer, AddBookSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

# Book Upload Operation
@swagger_auto_schema(method='POST', operation_summary='add new book', request_body=AddBookSerializer())
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def add_book(request):
    """ Book Upload Operation """
    
    if request.method == 'POST':
        serializer_class = BookSerializer(data=request.data)
        if serializer_class.is_valid():
            book_obj = Book.objects.create(**serializer_class.validated_data)
            serializer = BookSerializer(book_obj)
            context = {
                'status': True,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                'status': False,
                'message': 'Failed',
                'data': serializer_class.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

# Book Modification Operations
@swagger_auto_schema(method='GET', operation_summary='fetch a book')
@swagger_auto_schema(method='PUT', operation_summary='modify book properties', request_body=BookSerializer())
@swagger_auto_schema(method='DELETE', operation_summary='delete book', request_body=BookSerializer())
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def modify_book(request, book_title):
    """ Book Modification Operations """
    
    try:
        book_obj = Book.objects.get(title=book_title)
    except Book.DoesNotExist:
        context = {
            'status': False,
            'message': 'Book does not exist.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer_class = BookSerializer(book_obj)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer_class = BookSerializer(book_obj, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            context = {
                'status': True,
                'message': 'Success',
                'data': serializer_class.data
            }
            return Response(context, status=status.HTTP_202_ACCEPTED)
        else:
            context = {
                'status': False,
                'message': 'Failed',
                'error': serializer_class.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book_obj.delete()
        data = {
            'status'  : True,
            'message' : 'Deleted Successfully'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# Fetch All Available Books
@swagger_auto_schema(method='GET', operation_summary='fetch all books')
@api_view(['GET'])
def fetch_books(request):
    """ Fetch All Available Books """
    
    if request.method == 'GET':
        book_obj = Book.objects.all().order_by('title')
        serializer_class = BookSerializer(book_obj, many=True)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)

@swagger_auto_schema(method='GET', operation_summary='fetch book by book title')      
@api_view(['GET'])
def fetch_book_by_title(request, title):
    """ Fetch Book By Book Title"""
    
    try:
        book_obj = Book.objects.get(title=title)
    except Book.DoesNotExist:
        context = {
            'status': False,
            'message': 'Book does not exist.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer_class = BookDetailSerializer(book_obj)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)

# Fetch Book By Book Category
@swagger_auto_schema(method='GET', operation_summary='fetch book by book category')
@api_view(['GET'])
def fetch_book_by_category(request, category):
    """ Fetch Book By Book Category """
    
    try:
        print("Getting book by category")
        book_obj = Book.objects.filter(book_category__name=category)
    except Book.DoesNotExist:
        context = {
            'status': False,
            'message': 'Book does not exist.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer_class = BookSerializer(book_obj, many=True)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)

# Fetch Book By Book Author
@swagger_auto_schema(method='GET', operation_summary='fetch book by book author')
@api_view(['GET'])
def fetch_book_by_author(request, book_author):
    """ Fetch Book By Book Author """
    
    try:
        book_obj = Book.objects.get(author__name=book_author)
    except Book.DoesNotExist:
        context = {
            'status': False,
            'message': 'Book by {book_author} not found.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer_class = BookSerializer(book_obj, many=True)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)