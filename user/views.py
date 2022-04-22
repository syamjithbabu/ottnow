from django.shortcuts import redirect, redirect, render
from common.models import User
from ottnow.decorators import auth_customer

from user.models import UploadVideo

# Create your views here.
@auth_customer
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
        video_thumbnail = request.FILES['thumbnail']
        video_file = request.FILES['upload']
        user = User.objects.get(user_id = request.session['user'])

        upload_video = UploadVideo(video_title = video_title,video_genre = video_genre,video_description = video_description,video_duration = video_duration,language = language,video_file = video_file,video_thumbnail = video_thumbnail,user_id = user)
        upload_video.save()
        upload_msg = 'Your video is uploaded.Wait for the confirmation from admin.'
        # uploaded_video = UploadVideo.objects.filter(user_id = request.session['user'])
   
    return render(request,'upload_video.html',{'upload_msg':upload_msg})

def change_pw(request):
    msg = ""
    if request.method == "POST":
        oldpassword = request.POST['oldpw']
        newpassword = request.POST['newpw']
        confirmpassword = request.POST['cpw']

        user_data = User.objects.get(user_id=request.session['user'])
        if user_data.user_password == oldpassword:
            if newpassword == confirmpassword:
                User.objects.filter(user_id=request.session['user']).update(user_password=newpassword)
                msg = "Password Changed..!"
            else:
                msg = "Password Not Matching..!"
        else:
            msg = "Password Is Incorrect..!"
    return render(request,'changepassword.html',{'msg':msg,})

def user_logout(request):
    del request.session['user']
    request.session.flush()
    return redirect('common:login')