from rest_framework import serializers
from .models import Author, Book, Publisher, Product, Order

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'published_date']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
      orders = OrderSerializer(many=True, read_only=True)
      class Meta:
        model = Product
        fields = '__all__'
        