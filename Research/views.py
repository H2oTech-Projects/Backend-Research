from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer , UserSerializer
from rest_framework.views import APIView
from .utils import ServiceUnavailable
from rest_framework.exceptions import ValidationError ,  ParseError
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsAdminUser

class ProductDetailView(APIView):
  def get(self, request, pk):
    try:
      product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
      raise Http404  # DRF converts it into a 404 response
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  
  def delete(self, request, pk):
    try:
      product = Product.objects.get(pk=pk)
      product.delete()
      return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
      raise Http404

class ThirdPartyServiceView(APIView):
  def get(self, request):
    raise ServiceUnavailable()

class UserView(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
      raise ValidationError(serializer.errors)  
    return Response(serializer.validated_data)
  
class ExampleView(APIView):
  def post(self, request, *args, **kwargs):
    try:
      data = request.data 
    except ParseError:
      raise ParseError("Invalid JSON data provided.")
    return Response({"message": "Valid data received"}, status=200)

class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated user data"})
    
class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Welcome, admin!"})
