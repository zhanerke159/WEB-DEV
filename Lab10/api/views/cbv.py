from api.models import Product, Category
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import CategorySerializer, ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class ProductListAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True)
        Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None
        
    def get(self, request, product_id):
        product = self.get_object(product_id)
        if not product:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
            
        
    def put(self, request, product_id):
        product = self.get_object(product_id)
        if not product:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id): # Не забывай аргумент request!
        product = self.get_object(product_id)
        if not product:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

        

        
        

        

