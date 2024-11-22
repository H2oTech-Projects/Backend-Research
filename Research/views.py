from django.shortcuts import render

from django.http import JsonResponse
import os

def my_view(request):
    api_key = os.getenv('API_KEY')  # Access the API_KEY
    return JsonResponse({"message": f"Your API key is {api_key}"})