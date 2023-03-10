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
    path('ad_dashboard', views.ad_dashboard, name='ad_dashboard'),
    path('ad_create_work', views.ad_create_work, name='ad_create_work'),
    path('ad_view_work', views.ad_view_work, name='ad_view_work'),
    path('ad_view_clint', views.ad_view_clint, name='ad_view_clint'),
    path('ad_daily_work', views.ad_daily_work, name='ad_daily_work'),
    path('ad_daily_work_det', views.ad_daily_work_det, name='ad_daily_work_det'),
    #---------------------------------------------------------------------------Executive Section
    path('ex_base', views.ex_base, name='ex_base'),
    path('ex_profile', views.ex_profile, name='ex_profile'),
    path('ex_dashboard', views.ex_dashboard, name='ex_dashboard'),
    
]