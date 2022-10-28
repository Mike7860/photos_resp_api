import requests
import json
import os
from rest_framework import viewsets
from photos_app.serializers import PhotoSerializer, DeletePostSerializer, UpdatePostSerializer, AddPostSerializer
from photos_app.models import Photo
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class PhotoDeleteSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(album_ID=1)
    serializer_class = DeletePostSerializer
    http_method_names = ['delete', 'get']

    def destroy(self, request, pk=None, *args, **kwargs) -> HttpResponse:
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoUpdateSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(album_ID=1)
    serializer_class = UpdatePostSerializer
    http_method_names = ['put', 'get']

    def update(self, request, pk=None, *args, **kwargs) -> HttpResponse:
        instance = self.get_object()
        data = request.data
        instance.title = data["title"]
        instance.album_ID = data["album_ID"]
        instance.url = data["url"]
        instance.save()

        return Response(status=status.HTTP_200_OK)


class PhotoAddSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(album_ID=1)
    serializer_class = AddPostSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs) -> HttpResponse:
        data = request.data
        new_photo = Photo.objects.create(title=data["title"], album_ID=data["album_ID"], url=data["url"])
        new_photo.save()

        return Response(status=status.HTTP_201_CREATED)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(album_ID=1)
    serializer_class = PhotoSerializer
    http_method_names = ['get']


@api_view(['GET'])
def catch_photos_from_api(request: requests):
    photos = {}
    assert os.path.isfile("photos.json") is True
    with open("photos.json") as json_file:
        x = json.load(json_file)
    if len(x) > 0:
        data = x
        print("JSON source")
    else:
        response = requests.get("https://jsonplaceholder.typicode.com/photos")
        assert response.status_code == 200
        data = response.json()
        print("API source")

    for i in data:
        if "/600/" in str(i['url']):
            width = 600
            height = 600
        splitted_url = str(i['url']).split('/')
        dominant_color = splitted_url[-1]
        photo_data = Photo(
            album_ID=i['albumId'],
            id=i['id'],
            title=i['title'],
            url=i['url'],
            width=width,
            height=height,
            dominant_color=dominant_color
        )
        photo_data.save()
        photos = Photo.objects.all().order_by('-id')
    return render(request, 'photo_from_api.html', {"photos": photos})
