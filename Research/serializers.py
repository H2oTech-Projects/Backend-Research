from rest_framework import serializers
from .models import Book,Person,Author, Novel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= "__all__"

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields= "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields= "__all__"

class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Novel
        fields= "__all__"