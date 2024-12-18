from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class SwaggerAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Swagger!"})
    

class GoodbyeAPIView(APIView):
    def get(self, request):
        return Response({"message": "Goodbye, World!"})
