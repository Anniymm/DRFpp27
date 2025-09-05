from django.urls import path
from .views import *
urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name = 'product-list-create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestoryAPIView.as_view(), name = 'product-detail'),
]


