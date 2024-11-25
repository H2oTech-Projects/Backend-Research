from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Publisher, Product, Order
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer, ProductSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.models import User
from rest_framework import viewsets
#from .permissions import IsAuthor
from rest_framework.decorators import action
from django.http import Http404

'''class AuthorListCreateView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('author_pk')
        if author_id:
            return Book.objects.filter(author_id=author_id)
        return Book.objects.all()
    
    @action(detail=True)
    def publisher(self, request, pk=None):
        book = self.get_object()  # Fetch the book object by primary key (pk)
        publisher = book.publisher  # Get the publisher of the book
        publisher_serializer = PublisherSerializer(publisher)  # Serialize the publisher
        return Response(publisher_serializer.data)  # Return the serialized publisher data
    
    '''def perform_create(self, serializer):# Associate the current logged-in user as the author when creating a book
        serializer.save(author=self.request.user)'''

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class product_detail(APIView):
 
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrderListCreateView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(id=pk)  # Get the product by pk
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        orders = Order.objects.filter(product=product)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, pk, *args, **kwargs):
        # 'pk' is the product ID
        try:
            product = Product.objects.get(id=pk)  # Get the product by pk
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class order_detail(APIView):
    def get_object(self, order_pk):
        try:
            return Order.objects.get(id=order_pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        order = self.get_object(pk) 
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)