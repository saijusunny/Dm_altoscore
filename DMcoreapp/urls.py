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
    path('ad_work_analiz', views.ad_work_analiz, name='ad_work_analiz'),
    path('ad_work_analiz_ex', views.ad_work_analiz_ex, name='ad_work_analiz_ex'),
    path('ad_work_analiz_det', views.ad_work_analiz_det, name='ad_work_analiz_det'),
    path('ad_work_progress', views.ad_work_progress, name='ad_work_progress'),
    path('ad_work_progress_ex', views.ad_work_progress_ex, name='ad_work_progress_ex'),
    path('ad_work_progress_det', views.ad_work_progress_det, name='ad_work_progress_det'),
    path('ad_warning_ex', views.ad_warning_ex, name='ad_warning_ex'),
    path('ad_warning_det', views.ad_warning_det, name='ad_warning_det'),
    #---------------------------------------------------------------------------Executive Section
    path('ex_base', views.ex_base, name='ex_base'),
    path('ex_profile', views.ex_profile, name='ex_profile'),
    path('ex_dashboard', views.ex_dashboard, name='ex_dashboard'), 
    path('ex_daily_work_clint', views.ex_daily_work_clint, name='ex_daily_work_clint'), 
    path('ex_daily_work_det', views.ex_daily_work_det, name='ex_daily_work_det'),
    path('ex_weekly_rep_clint', views.ex_weekly_rep_clint, name='ex_weekly_rep_clint'),
    path('ex_weekly_rep_clint_det', views.ex_weekly_rep_clint_det, name='ex_weekly_rep_clint_det'),
    path('ex_view_work_clint', views.ex_view_work_clint, name='ex_view_work_clint'),
    path('ex_view_clint_det', views.ex_view_clint_det, name='ex_view_clint_det'),  
    path('ex_warning', views.ex_warning, name='ex_warning'),
    
]