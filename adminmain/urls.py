from django.urls import path
from . import views

app_name = 'adminmain'

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('users_profile',views.users_profile,name='users_profile'),
    path('upload_request',views.upload_request,name='upload_request'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('approve/<int:id>',views.approve,name='approve')
]
