
from django.urls import path
from .views import *

urlpatterns = [
    # path('',base,name='base'),
path('', home, name='home'),
path('about/', about, name='about'),
path('service/', service, name='service'),
path('content/', content, name='content'),
path('register/', register, name='register'),
path('login/', login, name='login'),
path('savedata/', savedata, name='savedata'),
path('logindata/', logindata, name='logindata'),


]
