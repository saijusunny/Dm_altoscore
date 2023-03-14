from django.shortcuts import render
from venv import create
import qrcode
import random
import os, json, math
# import psycopg2
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt
from django. contrib import messages
from unicodedata import name

from django.shortcuts import render, redirect
from .models import *
from datetime import datetime,date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.db.models import Q
from num2words import num2words

from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

#----------------------------------------------------------Login, Sign Up, Reset, Internshipform 
def login(request):
    return render(request, 'home/login.html')

def signin(request):
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            return redirect('login')
        
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],department="Admin",status="active").exists():
            member = user_registration.objects.get(email=request.POST['email'],password=request.POST['password'])
            
            request.session['userid'] = member.id
            
            return redirect('ad_profile')


        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],department="Digital Marketing Head",status="active").exists():
            member = user_registration.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['userid'] = member.id
            return redirect('hd_profile')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],department="Digital Marketing Executive",status="active").exists():
            member = user_registration.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['userid'] = member.id

            return redirect('ex_profile')
        else:
            return redirect('login')


           

def signup(request):
    return render(request, 'home/signup.html')

def registration_form(request):

 
    a = user_registration()
    b = qualification()
    c = extracurricular()

    if request.method == 'POST':
        if  user_registration.objects.filter(email=request.POST['email']).exists():
            
            msg_error = "Mail id already exist"
            return render(request, 'home/signup.html',{'msg_error': msg_error})
        else:
            
            a.fullname = request.POST['fname']
            a.fathername = request.POST['fathername']
            a.mothername = request.POST['mothername']
            a.dateofbirth = request.POST['dob']
            a.gender = request.POST['gender']
            a.presentaddress1 = request.POST['address1']
            a.presentaddress2  =  request.POST['address2']
            a.presentaddress3 =  request.POST['address3']
            a.pincode = request.POST['pincode']
            a.district  =  request.POST['district']
            a.state  =  request.POST['state']
            a.country  =  request.POST['country']
            a.permanentaddress1 = request.POST['paddress1']
            a.permanentaddress2  =  request.POST['paddress2']
            a.permanentaddress3  =  request.POST['paddress3']
            a.permanentpincode = request.POST['ppincode']
            a.permanentdistrict  =  request.POST['pdistrict']
            a.permanentstate  =  request.POST['pstate']
            a.permanentcountry =  request.POST['pcountry']
            a.mobile = request.POST['mobile']
            a.alternativeno = request.POST['alternative']
            a.department = request.POST['department']
            a.email = request.POST['email']
            a.status = "active"
            a.designation = request.POST['designation']
            a.password= random.SystemRandom().randint(100000, 999999)
            
            #a.branch_id = request.POST['branch']
            a.photo = request.FILES['photo']
            a.idproof = request.FILES['idproof']
            a.save()
            
            x = user_registration.objects.get(id=a.id)
            today = date.today()
            tim = today.strftime("%m%y")
            x.employee_id = "INF"+str(tim)+''+"B"+str(x.id)
            passw=x.password
            email_id=x.email
            x.save()
            y1 = user_registration.objects.get(id=a.id)
            qr = qrcode.make("http://altoscore.in/offerletter/" + str(y1.id))
            qr.save(settings.MEDIA_ROOT + "/images"+"//" +"offer"+str(y1.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"offer"+ str(y1.id) +".png","rb") as reopen:
                    djangofile = File(reopen)
                    y1.offerqr = djangofile
                    y1.save()
    
            y2 = user_registration.objects.get(id=a.id)
            qr1 = qrcode.make("http://altoscore.in/relieveletter/" + str(y2.id))
            qr1.save(settings.MEDIA_ROOT + "/images"+"//"+"re" +str(y2.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"re" + str(y2.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y2.relieveqr = djangofile
                    y2.save()
            y3 = user_registration.objects.get(id=a.id)
            qr2 = qrcode.make("http://altoscore.in/experienceletter/" + str(y3.id))
            qr2.save(settings.MEDIA_ROOT + "/images"+"//"+"exp" +str(y3.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"exp" + str(y3.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y3.expqr = djangofile
                    y3.save()
           
    
            b.user_id = a.id
            b.plustwo = request.POST.get('plustwo')
            b.school = request.POST['school']
            b.schoolaggregate = request.POST['aggregate']
            if request.FILES.get('cupload') is not None:
                b.schoolcertificate = request.FILES['cupload']
            b.ugdegree = request.POST['degree']
            b.ugstream = request.POST['stream']
            b.ugpassoutyr = request.POST['passoutyear']
            b.ugaggregrate = request.POST['aggregate1']
            b.backlogs = request.POST['supply']
            if request.FILES.get('cupload1') is not None:
                b.ugcertificate = request.FILES['cupload1']
            b.pg = request.POST['pg']
            b.save()
    
            c.user_id = a.id
            c.internshipdetails = request.POST['details']
            c.internshipduration = request.POST['duration']
            c.internshipcertificate = request.POST['certificate']
            c.onlinetrainingdetails = request.POST['details1']
            c.onlinetrainingduration = request.POST['duration1']
            c.onlinetrainingcertificate= request.POST['certificate1']
            c.projecttitle = request.POST['title']
            c.projectduration = request.POST['duration2']
            c.projectdescription = request.POST['description']
            c.projecturl = request.POST['url']
            c.skill1 = request.POST['skill1']
            c.skill2 = request.POST['skill2']
            c.skill3 = request.POST['skill3']
            c.save()
            
            subject = 'Greetings from ALTOS TECHNOLOGIES'
            message = 'Congratulations,\nYou have successfully registered ALTOS TECHNOLOGIES.\nYour login credentials \n\nEmail :'+str(email_id)+'\nPassword :'+str(passw)+'\n\nNote: This is a system generated email, do not reply to this email id.'
            email_from = settings.EMAIL_HOST_USER
            
            recipient_list = [email_id, ]
            send_mail(subject,message , email_from, recipient_list, fail_silently=True)
            msg_success = "Registration successfully Check Your Registered Mail"
            return redirect('login')
        
    return redirect('login')



def reset_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.get(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)

            _user.password = password
            subject = 'iNFOX Technologies your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)

            _user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Reset_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist iNFOX Technologies "
            return render(request, 'Reset_password.html', {'msg_error': msg_error})

    return render(request,'home/Reset_password.html')

def internshipform(request):
    # branch = branch_registration.objects.all()
    return render(request, 'home/internship.html')

def internship_save(request):

    a = internship()
    if request.method == 'POST':
        try:
            a.fullname = request.POST['name']
            a.collegename = request.POST['college_name']
            a.reg_date = datetime.now()
            a.reg_no = request.POST['reg_no']
            a.course = request.POST['course']
            a.stream = request.POST['stream']
            a.platform = request.POST['platform']

            a.start_date =  request.POST['start_date']
            a.end_date  =  request.POST['end_date']
            a.mobile  =  request.POST['mobile']

            a.alternative_no  =  request.POST['alternative_no']

            a.email = request.POST['email']
            a.profile_pic  =  request.FILES['profile_pic']
            if (a.end_date<a.start_date):
                return render(request,'home/internship.html',{'a':a})
            else:
                a.save()
                qr = qrcode.make("https://altoscore.in/admin_code?id=" + str(a.id))
                qr.save(settings.MEDIA_ROOT + "\\" +str(a.id) + ".png")
                with open(settings.MEDIA_ROOT + "\\" + str(a.id) + ".png", "rb") as reopen:
                        djangofile = File(reopen)
                        a.qr = djangofile

                        a.save()
           
            msg_success="Your application has been sent successfully"
            Flag='True'
            return render(request, 'home/internship.html',{'msg_success':msg_success})
        except:
            message = "Enter all details !!!"
            return render(request, 'home/internship.html',{'message':message})
    else:
        
        return render(request, 'home/internship.html')


# -----------------------------------------------------------------------------Admin Section

def ad_base(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_base.html',context)

def ad_profile(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_profile.html',context )

def ad_dashboard(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_dashboard.html',context)

def ad_create_work(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_create_work.html',context)

def save_create_work(request):
    clint = clint_information()
    if request.method == 'POST':
        clint.client_name = request.POST['client_name']
        clint.client_name = request.POST['client_address']
        clint.client_mail = request.POST['client_mail']
        clint.bs_name = request.POST['bs_name']
        clint.bs_website = request.POST['bs_website']
        clint.bs_location = request.POST['bs_location']
        clint.client_files = request.FILES['client_files']
        clint.seo = request.POST['seo']
        clint.seo_txt = request.POST['seo_txt']
        clint.seo_file = request.FILES['seo_file']
        clint.smm = request.POST['smm']
        clint.smm_txt = request.POST['smm_txt']
        clint.smm_file = request.FILES['smm_file']
        clint.sem = request.POST['sem']
        clint.sem_txt = request.POST['sem_txt']
        clint.sem_file = request.FILES['sem_file']
        clint.em = request.POST['em']
        clint.em_txt = request.POST['em_txt']
        clint.em_file = request.FILES['em_file']
        clint.cm = request.POST['cm']
        clint.cm_txt = request.POST['cm_txt']
        clint.cm_file = request.FILES['cm_file']
        clint.am = request.POST['am']
        clint.am_txt = request.POST['am_txt']
        clint.am_file = request.FILES['am_file']
        clint.mm = request.POST['mm']
        clint.mm_txt = request.POST['mm_txt']
        clint.mm_file = request.FILES['mm_file']
        clint.vm = request.POST['vm']
        clint.vm_txt = request.POST['vm_txt']
        clint.vm_file = request.FILES['vm_file']
        clint.user=request.session['userid']
        clint.save()
        msg_success = "Save Successfully"
        return render(request, 'admin/ad_create_work.html',{'msg_success':msg_success})
    return redirect("ad_create_work")


def ad_view_work(request):
    return render(request, 'admin/ad_view_work.html')

def ad_view_clint(request):
    return render(request, 'admin/ad_view_clint.html')


def ad_daily_work_det(request):
    return render(request, 'admin/ad_daily_work_det.html')


def ad_work_analiz_det(request):
    return render(request, 'admin/ad_work_analiz_det.html')

def ad_work_progress(request):
    return render(request, 'admin/ad_work_progress.html')



def ad_work_progress_det(request):
    return render(request, 'admin/ad_work_progress_det.html') 

def ad_warning_ex(request):
    return render(request, 'admin/ad_warning_ex.html')

def ad_warning_sugg_dash(request):
    return render(request, 'admin/ad_warning_sugg_dash.html')

def ad_warning_det(request):
    return render(request, 'admin/ad_warning_det.html') 

def ad_suggestions_det(request):
    return render(request, 'admin/ad_suggestions_det.html')

# -----------------------------------------------------------------------------Executive Section

def ex_base(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'executive/ex_base.html',context)

def ex_profile(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'executive/ex_profile.html',context)

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

def ex_warnings_dash(request):
    return render(request, 'executive/ex_warnings_dash.html') 


def ex_warning(request):
    return render(request, 'executive/ex_warning.html')

def ex_suggestions(request):
    return render(request, 'executive/ex_suggestions.html')


    
