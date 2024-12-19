from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import Book
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class SwaggerAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Swagger!"})
    

class GoodbyeAPIView(APIView):
    def get(self, request):
        return Response({"message": "Goodbye, World!"})





class BookListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={201: BookSerializer(), 400: "Bad Request"}
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPIView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                serializer = BookSerializer(book)
                return Response(serializer.data)
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={200: BookSerializer(), 400: "Bad Request", 404: "Not Found"}
    )

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

