from category.models import Category
from category.serializers import CategoryDetailSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Fetch Book Categories
@swagger_auto_schema(method='GET', operation_summary='fetch all book categories')
@api_view(['GET'])
def category(request):
    """ Fetch Book Categories """
    
    if request.method == 'GET':
        category_obj = Category.objects.all().order_by('name')
        serializer_class = CategoryDetailSerializer(category_obj, many=True)
        context = {
            'status': True,
            'message': 'Success',
            'data': serializer_class.data
        }
        return Response(context, status=status.HTTP_200_OK)
