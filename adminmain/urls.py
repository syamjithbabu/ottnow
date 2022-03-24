from django.urls import path
from . import views

app_name = 'adminmain'

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('users_profile',views.users_profile,name='users_profile'),
    path('upload_request',views.upload_request,name='upload_request')
]
