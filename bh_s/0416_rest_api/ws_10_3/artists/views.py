from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer, ArtistUnitSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 사용자가 보낸 수정 데이터로 변환. + partial이 True여야 부분 수정 가능.
        serializer = ArtistUnitSerializer(artist, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        artist.delete()
        message = {f'delete : 등록 번호 {artist_pk}번의 {artist.name}을 삭제하였습니다.'}
        return Response(message,status=status.HTTP_204_NO_CONTENT)