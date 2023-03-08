from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('internshipform', views.internshipform, name='internshipform'),
    #---------------------------------------------------------------------------Admin Section
    path('ad_base', views.ad_base, name='ad_base'),
    path('ad_profile', views.ad_profile, name='ad_profile'),
    #---------------------------------------------------------------------------Executive Section
    path('ex_base', views.ex_base, name='ex_base'),
    path('ex_profile', views.ex_profile, name='ex_profile'),
    
]