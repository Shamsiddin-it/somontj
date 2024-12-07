from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]