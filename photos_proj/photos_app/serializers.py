from rest_framework import serializers

from photos_app.models import Photo


class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'album_ID', 'url')


class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'album_ID', 'width', 'height', 'dominant_color', 'url')


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'album_ID', 'url')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'album_ID', 'width', 'height', 'dominant_color', 'url')



