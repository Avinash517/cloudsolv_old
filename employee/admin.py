from django.contrib import admin
from django.contrib import admin
from .models import employeedetails,employee_personaldetails,employee_educationaldetails,employee_experiencedetails,applied_leaves,weeklyactivity,employee_attendance
# Register your models here.
admin.site.site_header = "Cloudsolv Administration"
admin.site.site_title = " Cloudsolv "
#admin.site.register([empdetails] )
admin.site.register([employee_educationaldetails,employee_personaldetails,employee_experiencedetails,applied_leaves,employeedetails,weeklyactivity,employee_attendance])