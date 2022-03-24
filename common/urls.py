from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('signup',views.sign_up,name='sign_up'),
    path('login',views.login,name='login'),
]
