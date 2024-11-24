from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.models import User
from rest_framework import viewsets
from .permissions import IsAuthor

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
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('author_pk')
        if author_id:
            # Filter books based on the 'author_id' in the URL
            return Book.objects.filter(author_id=author_id)
        return Book.objects.all()
    
    def perform_create(self, serializer):# Associate the current logged-in user as the author when creating a book
        serializer.save(author=self.request.user)