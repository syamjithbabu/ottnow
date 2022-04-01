from django.shortcuts import render

from user.models import UploadVideo

# Create your views here.

def user_home(request):
    return render(request,'user_home.html')

def payment(request):
    return render(request,'payment.html')

def payment_form(request):
    return render(request,'payment_form.html')

def upload_video(request):
    upload_msg = ''
    if request.method == "POST":
        video_title = request.POST['title']
        video_genre = request.POST['genre']
        video_description = request.POST['description']
        video_duration = request.POST['duration']
        language = request.POST['language']
        video_file = request.FILES['upload']
    
        # user = UploadVideo.objects.get(user_id=request.session['user'])

        upload_video = UploadVideo(video_title = video_title,video_genre = video_genre,video_description = video_description,video_duration = video_duration,language = language,video_file = video_file)
        upload_video.save()
        upload_msg = 'Your video is uploaded.Wait for the confirmation from admin.'
   
    return render(request,'upload_video.html',{'upload_msg':upload_msg})