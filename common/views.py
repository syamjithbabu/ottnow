from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request,'main_page.html')

def login(request):
    return render(request,'login.html')

def sign_up(request):
    return render(request,'sign_up.html')
