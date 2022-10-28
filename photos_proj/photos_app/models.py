from django.db import models

# Create your models here.
# We want to store photo title, album ID, width, height and dominant color (as a hex code) in local
# database;


class Photo(models.Model):
    # idd = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    album_ID = models.CharField(max_length=100)
    width = models.IntegerField(default=600)
    height = models.IntegerField(default=600)
    dominant_color = models.CharField(max_length=100, default="ffffff")
    url = models.URLField(max_length=200, null=True, blank=True)
    #thumbnailUrl = models.CharField(max_length=100)
