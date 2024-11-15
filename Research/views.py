from django.http import JsonResponse
from .models import drink 
from .serializers import drinkserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET' , 'POST'])
def drink_list(request , format = None):
    if request.method == 'GET':
        drinks = drink.objects.all()  
        serializer = drinkserializer(drinks, many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer = drinkserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

@api_view(['GET' , 'PUT' , 'DELETE'])
def drink_detail(request, id ,format = None):

    try:
        drinks = drink.objects.get(pk=id)
    except drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = drinkserializer(drinks)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = drinkserializer(drinks , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)