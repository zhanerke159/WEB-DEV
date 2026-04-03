from django.urls import path
from api import views

urlpatterns = [
    path('/products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
    
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),
    
    path('categories/<int:category_id>/products/', views.CategoryProductsAPIView.as_view()),
]