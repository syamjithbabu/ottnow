from django.shortcuts import render

# Create your views here.

def user_home(request):
    return render(request,'user_home.html')

def payment(request):
    return render(request,'payment.html')

def payment_form(request):
    return render(request,'payment_form.html')

def upload_video(request):
    return render(request,'upload_video.html')