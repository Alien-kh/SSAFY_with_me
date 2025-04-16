from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer


# Create your views here.
@api_view(['POST', 'GET'])
def artist_list_or_create(request):
    # POST(생성)
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # GET(조회)
    elif request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
