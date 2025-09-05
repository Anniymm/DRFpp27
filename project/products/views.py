# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# APIView - bevri kodi - sruli kontroli - custom/complex apis 
# GenericAPIView + Mixins - sashualo - susti vidre apiviews-ebs - mkacrad rom maqvs gansazghvruli rac mwhirdeba
# konkretuli Generic view - cota - medium - martivi CRUD operaciebistvis 
# ViewSets - yvelazecota - medium - complex/did proeqtebshi 

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# get, post, put, delete


# Product CRUD - get, post, delete, put
# konkretuli Generic view - cota - medium - martivi CRUD operaciebistvis 

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Product, ProductLog
from .serializers import ProductLogSerializer, ProductSerializer      # *

# - get - yvela productistvis
# - post - axali producqtis sheqmna
# class ProductListCreateView(generics.ListCreateAPIView):    # /products/
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [AllowAny] 

#     def perform_create(self, serializer):
#         serializer.save()  # damattebiti logikebic shemidzlia, 

# # get - /products/<id> - erti konkretuli 
# # put - /products/<id>- productis srulad cvlileba
# # patch - /products/<id>- productis nawilobriv cvlileba
# # delete = /products/<id> - washla

# class ProductRetrieveUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [AllowAny]

# ////////////////////////////////////////////////////////////////////////////////////////////
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# APIView
# - get - yvela productistvis
# - post - axali producqtis sheqmna
class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# # get - /products/<id> - erti konkretuli 
# # put - /products/<id>- productis srulad cvlileba
# # patch - /products/<id>- productis nawilobriv cvlileba
# # delete = /products/<id> - washla

class ProductRetrieveUpdateDestoryAPIView(APIView):

    def get_object(self, pk):  # erti cali konkretuli productis wamogheba
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
        
    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 

    


