from contextlib import redirect_stderr, redirect_stdout
from django.shortcuts import redirect, render

from common.models import User, AdminMain
from . models import *
# Create your views here.

def main_page(request):
    return render(request,'main_page.html')

def sign_up(request):
    user_msg = ''
    if request.method == 'POST':
        user_first_name = request.POST['first_name']
        user_second_name = request.POST['second_name']
        user_age = request.POST['age']
        user_email = request.POST['user_email']
        user_password = request.POST['password']

        email_exist = User.objects.filter(user_email = user_email).exists()

        if not email_exist:
            new_user = User(user_first_name = user_first_name,user_second_name = user_second_name,user_age = user_age,user_email = user_email,user_password = user_password)
            new_user.save()
            user_msg = 'Your account is created...'
        else:
            user_msg = 'This email is already exist...'
    return render(request,'sign_up.html',{'user_msg':user_msg,})

def login(request):
    user_msg2 = ""
    if request.method == "POST":
        email = request.POST['user_email']
        password = request.POST['user_password']

        user_exist = User.objects.filter(user_email = email,user_password = password).exists()
        admin_exist = AdminMain.objects.filter(admin_email = email,admin_password = password).exists()


        if user_exist:
            user_data = User.objects.get(user_email = email,user_password = password) #by using get we get a single data
            request.session['user'] = user_data.user_id
            return redirect('user:user_home')
        if admin_exist:
            admin_data = AdminMain.objects.get(admin_email = email,admin_password = password)
            request.session['admin'] = admin_data.admin_id
            return redirect('adminmain:admin_home')
        else:
            user_msg2 = 'Incorrect Password!'
    return render(request,'login.html',{'user_msg':user_msg2,})




