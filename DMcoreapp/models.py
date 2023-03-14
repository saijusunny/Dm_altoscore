from django.db import models
from email.policy import default
from turtle import delay
from unittest.util import _MAX_LENGTH
from xmlrpc.client import boolean
from django.contrib.auth.models import User

# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
# Create your models here.


# login

class user_registration(models.Model):
    designation = models.CharField(max_length=240, null=True)
    department = models.CharField(max_length=240, null=True)
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    employee_id = models.CharField(max_length=240,null=True,default='')
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default="active")
    tl_id = models.IntegerField(default='0',null=True, blank=True)
    projectmanager_id = models.IntegerField(default='0',null=True, blank=True)
    total_pay=models.IntegerField(default='0')
    payment_balance = models.IntegerField( default='0')
    account_no = models.CharField(max_length=200, null=True,blank=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True,blank=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')
    payment_status = models.CharField(max_length=200, null=True, default='')
    offerqr = models.CharField(max_length=500, default='',null=True,blank=True)
    relieveqr = models.CharField(max_length=500, default='',null=True,blank=True)
    expqr = models.CharField(max_length=500, default='',null=True,blank=True)
    hrmanager = models.CharField(max_length=500, default='',null=True,blank=True)
    confirm_salary = models.CharField(max_length=10, default='')
    confirm_salary_status = models.CharField(max_length=255, default='0')
    payment_file_downlod = models.FileField(upload_to = 'images/', null=True, blank=True)
    total_amount=models.IntegerField(default='0')
    payment_amount_date =models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    salary_pending = models.CharField(max_length=100, default='')
    salary_status =  models.CharField(max_length=10, default='')
    trainer_level = models.CharField(max_length=20, default='',null=True, blank=True)
    hr_designation = models.CharField(max_length=120, default='',null=True, blank=True)
    reg_status =  models.CharField(max_length=10, default='0')
    trainee_delay=models.IntegerField(default=0)
 
    def __str__(self):
        return self.fullname

    @property
    def avg(self):
        return (self.attitude+self.creativity+self.workperformance)/3

class qualification(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='qualificationuser', null=True, blank=True)
    plustwo = models.CharField(max_length=240, null=True)
    schoolaggregate = models.CharField(max_length=240, null=True)
    schoolcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    ugdegree = models.CharField(max_length=240, null=True)
    ugstream = models.CharField(max_length=240, null=True)
    ugpassoutyr = models.CharField(max_length=240, null=True)
    ugaggregrate = models.CharField(max_length=240, null=True)
    backlogs = models.CharField(max_length=240, null=True)
    ugcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    pg = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.user

class extracurricular(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='extracurricularuser', null=True, blank=True)
    internshipdetails = models.CharField(max_length=240, null=True)
    internshipduration = models.CharField(max_length=240, null=True)
    internshipcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    onlinetrainingdetails = models.CharField(max_length=240, null=True)
    onlinetrainingduration = models.CharField(max_length=240, null=True)
    onlinetrainingcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    projecttitle = models.CharField(max_length=240, null=True)
    projectduration = models.CharField(max_length=240, null=True)
    projectdescription = models.TextField(null=True)
    projecturl = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill1 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill2 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill3 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    status = models.CharField(max_length=240, default='')


    def __str__(self):
        return self.projecttitle

class internship(models.Model):

    reg_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    fullname = models.CharField(max_length=200)
    collegename = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    stream = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    alternative_no = models.CharField(max_length=200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='images/internship/', null=True, blank=True)
    qr = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.fullname

class clint_information(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True, blank=True)
    client_name = models.CharField(max_length=200,default='', null=True, blank=True)
    client_address = models.CharField(max_length=200,default='', null=True, blank=True)
    client_mail = models.CharField(max_length=200,default='', null=True, blank=True)
    bs_name = models.CharField(max_length=200,default='', null=True, blank=True)
    bs_website = models.CharField(max_length=200,default='', null=True, blank=True)
    bs_location = models.CharField(max_length=200,default='', null=True, blank=True)
    client_files = models.ImageField(upload_to='images/client/', null=True, blank=True)
    seo = models.CharField(max_length=200,default='', null=True, blank=True)
    seo_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    seo_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    smm = models.CharField(max_length=200,default='', null=True, blank=True)
    smm_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    smm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    sem = models.CharField(max_length=200,default='', null=True, blank=True)
    sem_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    sem_file =models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    em = models.CharField(max_length=200,default='', null=True, blank=True)
    em_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    em_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    cm = models.CharField(max_length=200,default='', null=True, blank=True)
    cm_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    cm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    am = models.CharField(max_length=200,default='', null=True, blank=True)
    am_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    am_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    mm = models.CharField(max_length=200,default='', null=True, blank=True)
    mm_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    mm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    vm = models.CharField(max_length=200,default='', null=True, blank=True)
    vm_txt = models.CharField(max_length=200,default='', null=True, blank=True)
    vm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)