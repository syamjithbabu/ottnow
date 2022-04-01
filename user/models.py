from django.db import models

# Create your models here.

class UploadVideo(models.Model):
    video_title = models.CharField(max_length=50)
    video_genre = models.CharField(max_length=20)
    video_description = models.CharField(max_length=200)
    video_duration = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    video_file = models.FileField(upload_to='uploaded_files/')

    class Meta:
        db_table = 'upload_files'