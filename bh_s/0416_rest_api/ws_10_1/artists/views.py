# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Artist
from .serializers import ArtistSerializer

# Create your views here.
@api_view(['POST'])
def artist_list(request):
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


