from django.shortcuts import render

# Create your views here.

#----------------------------------------------------------Login, Sign Up, Reset, Internshipform 
def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')

def reset_password(request):
    return render(request,'home/Reset_password.html')

def internshipform(request):
    # branch = branch_registration.objects.all()
    return render(request, 'home/internship.html')

# -----------------------------------------------------------------------------Admin Section

def ad_base(request):
    return render(request, 'admin/ad_base.html')

def ad_profile(request):
    return render(request, 'admin/ad_profile.html')

def ad_dashboard(request):
    return render(request, 'admin/ad_dashboard.html')

def ad_create_work(request):
    return render(request, 'admin/ad_create_work.html')

def ad_view_work(request):
    return render(request, 'admin/ad_view_work.html')

def ad_view_clint(request):
    return render(request, 'admin/ad_view_clint.html')


def ad_daily_work(request):
    return render(request, 'admin/ad_daily_work.html')

def ad_daily_work_det(request):
    return render(request, 'admin/ad_daily_work_det.html')

def ad_work_analiz(request):
    return render(request, 'admin/ad_work_analiz.html')
def ad_work_analiz_ex(request):
    return render(request, 'admin/ad_work_analiz_ex.html')

def ad_work_analiz_det(request):
    return render(request, 'admin/ad_work_analiz_det.html')

def ad_work_progress(request):
    return render(request, 'admin/ad_work_progress.html')

def ad_work_progress_ex(request):
    return render(request, 'admin/ad_work_progress_ex.html')

def ad_work_progress_det(request):
    return render(request, 'admin/ad_work_progress_det.html') 

def ad_warning_ex(request):
    return render(request, 'admin/ad_warning_ex.html')

def ad_warning_det(request):
    return render(request, 'admin/ad_warning_det.html')

# -----------------------------------------------------------------------------Executive Section

def ex_base(request):
    return render(request, 'executive/ex_base.html')

def ex_profile(request):
    return render(request, 'executive/ex_profile.html')

def ex_dashboard(request):
    return render(request, 'executive/ex_dashboard.html')

def ex_daily_work_clint(request):
    return render(request, 'executive/ex_daily_work_clint.html')

def ex_daily_work_det(request):
    return render(request, 'executive/ex_daily_work_det.html')

def ex_weekly_rep_clint(request):
    return render(request, 'executive/ex_weekly_rep_clint.html')

def ex_weekly_rep_clint_det(request):
    return render(request, 'executive/ex_weekly_rep_det.html')

def ex_view_work_clint(request):
    return render(request, 'executive/ex_view_work_clint.html')

def ex_view_clint_det(request):
    return render(request, 'executive/ex_view_clint_det.html')


def ex_warning(request):
    return render(request, 'executive/ex_warning.html')


    
