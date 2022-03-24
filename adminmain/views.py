from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'admin_home.html')

def users_profile(request):
    return render(request,'users_profile.html')

def upload_request(request):
    return render(request,'upload_request.html')