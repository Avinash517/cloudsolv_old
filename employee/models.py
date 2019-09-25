from django.db import models
import datetime
# Create your models here.


#employe signup admin side

class employeedetails(models.Model):
    employee_id = models.PositiveIntegerField(primary_key=True)
    employee_name = models.CharField(max_length=30)
    employee_email = models.EmailField(max_length=100)
    employee_password = models.CharField(max_length=12)

    class Meta:
        db_table='employeedetails'

    def __str__(self):
        return str(self.employee_id)


#employe login

class employee_attendance(models.Model):
    session_id=models.AutoField(primary_key=True)
    login_date = models.DateField(blank=True)
    login_time = models.TimeField(auto_now_add=True)
    logout_time = models.TimeField(blank=True,null=True)
    status=models.CharField(max_length=20,blank=True,null=True)
    employee = models.OneToOneField(employeedetails,on_delete=models.CASCADE)

    class Meta:
        db_table='attendance'



#employee profile

class employee_personaldetails(models.Model):
    gender_choices = (('Male',"M"),('Female',"F"),('Others',"Others"))
    employee_image = models.ImageField()
    joining_date  = models.DateField()
    designation =  models.CharField(max_length=50)
    empoyee_dob =  models.DateField()
    father_name = models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=20,default='Male',choices=gender_choices)
    maritial_status = models.CharField(max_length=15)
    spouse_name = models.CharField(max_length=15,blank=True,null=True)
    children = models.IntegerField(null=True,blank=True)
    aadhar_number = models.BigIntegerField()
    upload_aadhar = models.FileField()
    pan_number = models.CharField(max_length=15)
    upload_pancard = models.FileField()
    passport_number = models.CharField(max_length=15,blank=True,null=True)
    drivinglicense_number = models.CharField(max_length=20,blank=True,null=True)
    upload_drivinglicense = models.FileField(blank=True,null=True)
    is_drivinglicense_uploaded = models.BooleanField(default=False)
    upload_passport = models.FileField(blank=True,null=True)
    is_passport_uploaded=models.BooleanField(default=False)
    voter_id_number = models.CharField(max_length=15,blank=True,null=True)
    upload_voterid = models.FileField(blank=True,null=True)
    is_Voterid_uploaded = models.BooleanField(default=False)
    Address1 = models.CharField(max_length=300)
    Address2 = models.CharField(max_length=300,blank=True,null=True)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    postal_code = models.IntegerField(null=True)
    telephone = models.BigIntegerField(null=True,blank=True)
    mobile_number = models.BigIntegerField(null=True)
    relatives_name=models.CharField(max_length=15)
    relation = models.CharField(max_length=15,blank=True,null=True)
    relative_address=models.CharField(max_length=200,blank=True,null=True)
    phone_number = models.BigIntegerField(null=True,blank=True)
    relative_mobile_number=models.BigIntegerField(null=True)
    employee=models.OneToOneField(employeedetails,on_delete=models.CASCADE)

    class Meta:
        db_table='personal_details'

    def  __str__(self):
        return self.employee.employee_name


#education details
class employee_educationaldetails(models.Model):
    tenth_schoolname = models.CharField(max_length=20,blank=True)
    tenth_schoolboard = models.CharField(max_length=20,blank=True)
    tenth_percentage = models.CharField(max_length=3,blank=True)
    tenth_cerificate = models.FileField(blank=True)
    inter_collegename = models.CharField(max_length=20,blank=True)
    inter_board = models.CharField(max_length=20,blank=True)
    inter_percentage = models.CharField(max_length=3,blank=True)
    inter_cerificate = models.FileField(blank=True)
    graduation_collegename = models.CharField(max_length=20,blank=True)
    graduation_board = models.CharField(max_length=20,blank=True)
    graduation_percentage = models.CharField(max_length=3,blank=True)
    graduation_cerificate = models.FileField(blank=True)
    postgraduation_collegename = models.CharField(max_length=20, blank=True)
    postgraduation_board = models.CharField(max_length=20, blank=True)
    postgraduation_percentage = models.CharField(max_length=3, blank=True)
    postgraduation_cerificate = models.FileField(blank=True)
    is_post_graduationcertificate_uploaded=models.BooleanField(default=False)
    employee=models.OneToOneField(employeedetails,on_delete=models.CASCADE,primary_key=True)

    class Meta:
        db_table='education_details'







#experience details
class employee_experiencedetails(models.Model):
    name_of_organisation = models.CharField(max_length=30)
    job_role = models.CharField(max_length=20)
    period_of_work = models.CharField(max_length=20)
    package = models.BigIntegerField(null=True)
    total_experience = models.CharField(max_length=20)
    forms_any = models.FileField(blank=True,null=True)
    is_form_any_uploaded=models.BooleanField(default=False)
    relieving_letter = models.FileField(null=False)
    pay_slip = models.FileField(null=False)
    name_of_organisation1= models.CharField(max_length=30,null=True)
    job_role1 = models.CharField(max_length=20,null=True)
    period_of_work1 = models.CharField(max_length=20,null=True)
    package1 = models.BigIntegerField(null=True)
    total_experience1 = models.CharField(max_length=20,blank=True,null=True)
    forms_any1 = models.FileField(blank=True, null=True)
    is_form_any_uploaded1 = models.BooleanField(default=False)
    relieving_letter1 = models.FileField(null=True,blank=True)
    is_relivingletter_uploaded = models.BooleanField(default=False)
    pay_slip1 = models.FileField(null=True)
    is_pay_slip1 = models.BooleanField(default=False)
    employee=models.OneToOneField(employeedetails,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table='experience_details'





#salary details
'''class employee_salary(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_designation = models.CharField(max_length=30)
    emp_location = models.CharField(max_length=20)
    emp_bankaccno = models.PositiveIntegerField()
    emp_bankname = models.CharField(max_length=20)
    emp_bankbranch = models.CharField(max_length=12)
    emp_bankifscno = models.CharField(max_length=10)
    emp_dateofjoining = models.DateField()
    emp_panno = models.CharField(max_length=10)
    emp_pfno = models.CharField(max_length=20)
    emp_esino = models.CharField(max_length=8)
    emp_passportno = models.CharField(max_length=20)'''


class applied_leaves(models.Model):
    c=(('pending',"pndg"),('sactioned',"yes"),('rejected',"no"))
    d=(('sick_leave',"Sick_Leave"),('casual_leave',"Casual_Leave"))
    leave_type = models.CharField(max_length=20,default='casual_leave',choices=d)
    reason=models.CharField(max_length=15)
    from_date=models.DateField()
    to_date=models.DateField()
    no_of_days = models.CharField(max_length=50)
    applied_by=models.ForeignKey(employeedetails,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,default='pending',choices=c)

    class Meta:
        db_table='applied_leaves'
    def __str__(self):
        return str(self.applied_by.employee_name)

#employe activity

class weeklyactivity(models.Model):
    complete_choice = (('Yes', 'yes'), ('No', 'no'))
    week_choices=(('monday',"monday"),('tuesday',"tuesday"),('wednesday',"wednesday"),('thursday',"thursday"),('friday',"friday"))
    week=models.CharField(max_length=9,choices=week_choices,null=True,blank=True)
    activity=models.TextField(null=True,blank=True)
    goal=models.CharField(max_length=6,choices=complete_choice,null=True,blank=True,default='')
    employee=models.ForeignKey(employeedetails,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table='weeklyacitivies'

    def __str__(self):
        return self.week
