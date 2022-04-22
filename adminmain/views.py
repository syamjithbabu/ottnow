from django.shortcuts import redirect, render
from common.models import AdminMain, User

from user.models import UploadVideo

# Create your views here.

def admin_home(request):
    upload = User.objects.filter(status = 'requested')
    return render(request,'admin_home.html',{'upload':upload})

def users_profile(request):
    users = AdminMain.objects.get(admin_id = request.session['admin'])
    profiles = User.objects.all()
    return render(request,'users_profile.html',{'user':users,'profiles':profiles})

def upload_request(request):
    users = AdminMain.objects.get(admin_id = request.session['admin'])
    uploads = UploadVideo.objects.all()
    return render(request,'upload_request.html',{'user':users,'uploads':uploads,})

def approve(request, id):
    status = 'Approved'
    User.objects.filter(user_id = id).update(status = status)
    return redirect('adminmain:admin_home')

def admin_logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('common:login')