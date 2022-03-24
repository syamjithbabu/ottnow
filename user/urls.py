from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('user_home',views.user_home,name='user_home'),
    path('payment',views.payment,name='payment'),
    path('payment_form',views.payment_form,name='payment_form'),
    path('upload_video',views.upload_video,name='upload_video')
]
