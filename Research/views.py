from django.shortcuts import render
from .serializers import BookSerializer,PersonSerializer,NovelSerializer,AuthorSerializer
from .models import Book,Person,Novel,Author
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookView(APIView):
    def get(self, request):
        books=Book.objects.all()
        serializer =BookSerializer(books,  many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IndiBookView(APIView):
    def get(self, request):
        indi_books=Book.indi_objects.all()
        serializer =BookSerializer(indi_books,  many=True)
        return Response(serializer.data)   
    
class IndiSpecificBookView(APIView):
    def get(self, request):
        specific_books = Book.indi_objects.filter(title="short life 1")
        serializer = BookSerializer(specific_books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        indi_count = Book.indi_objects.count()
        return Response({"count": indi_count}, status=status.HTTP_200_OK)


class PersonView(APIView):
    def get(self, request):
        persons=Person.people.all()
        serializer =PersonSerializer(persons,  many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorView(APIView):
    def get (self, request):
        authors = Person.authors.all()
        serializer=PersonSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EditorView(APIView):
    def get (self, request):
        editors = Person.editors.all()
        serializer=PersonSerializer(editors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AvailableAuthorsView(APIView):
    def get(self, request):
        available_authors = Author.objects.all()  # Uses AvailableManager by default
        serializer = AuthorSerializer(available_authors, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View to retrieve all books along with their authors
class NovelListView(APIView):
    def get(self, request):
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = NovelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BaseAuthorsView(APIView):
    def get(self, request):
        all_authors = Author._base_manager.all()  # Uses AvailableManager by default
        serializer = AuthorSerializer(all_authors, many=True)
        return Response(serializer.data)