# Generated by Django 4.0.3 on 2022-04-06 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=50)),
                ('video_genre', models.CharField(max_length=20)),
                ('video_description', models.SlugField(max_length=255)),
                ('video_duration', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('video_thumbnail', models.FileField(upload_to='thumbanail/')),
                ('video_file', models.FileField(upload_to='uploaded_files/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'upload_files',
            },
        ),
    ]
