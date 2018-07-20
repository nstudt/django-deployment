from django.conf.urls import url
# from django.contrib import admin
from app5 import views
from django.urls import path, re_path

#TEMPLATE taggin
app_name = 'app5'

urlpatterns=[
    re_path(r'^user_login/$',views.user_login,name='user_login'),
    re_path(r'^register/$', views.register, name = 'register' ),
    re_path(r'^special/',views.special,name='special'),
]