from api.models import Product, Category
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import CategorySerializer, ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def product_list(request):
    if request == 'GET':
         product = Product.objects.all()
         serializer = ProductSerializer(product,many = True)
         return Response(serializer.data)
       
    
    elif request == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request=='GET':
        serializer = ProductSerializer(product,pk = product_id)
        return Response(serializer.data)
    elif request == 'PUT':
        serializer = ProductSerializer(instance = product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    



