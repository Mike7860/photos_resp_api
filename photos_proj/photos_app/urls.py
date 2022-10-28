from django.urls import include, path

from rest_framework import routers

from photos_app.views import PhotoViewSet, PhotoDeleteSet, PhotoUpdateSet, PhotoAddSet, catch_photos_from_api

router = routers.DefaultRouter()
router.register(r'photo', PhotoViewSet)
router.register(r'delete', PhotoDeleteSet)
router.register(r'update', PhotoUpdateSet)
router.register(r'add', PhotoAddSet)

# /download endpoint used for save info about photos from API/json file to database
urlpatterns = [
   path('', include(router.urls)),
   path('download/', catch_photos_from_api, name="catch_photos_from_api"),
]