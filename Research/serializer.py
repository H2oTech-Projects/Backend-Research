from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'

# serializers.py
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()




