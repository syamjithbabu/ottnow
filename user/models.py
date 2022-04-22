from django.db import models

from common.models import User

# Create your models here.

class UploadVideo(models.Model):
    video_title = models.CharField(max_length=50)
    video_genre = models.CharField(max_length=20)
    video_description = models.SlugField(max_length=255)
    video_duration = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    video_thumbnail = models.ImageField(upload_to='thumbanail/')
    video_file = models.FileField(upload_to='uploaded_files/')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'upload_files'