"""cloudsolv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('addemp/',views.addemployee),
    path('', views.login),
    path('Signup/',views.signup),
    path('logout/', views.logout),
    path('attendence/',views.myattendance),
    path('monthlyattendence/',views.monthlyattendance),
    path('personaldetails/',views.personaldetails),
    path('editpersonal/', views.editpersonaldetails),
    path('updatepersonal/', views.updatepersonaldetails),
    path('education/', views.educationdetails),
    path('editeducation/', views.editeducationaldetails),
    path('updateeducation/', views.updateeducationaldetails),
    path('experience/', views.experiencedetails),
    path('editexperience/', views.editexperiencedetails),
    path('updateexperience/', views.updateexperiencedetails),
    path('changepsw/', views.changepassword),
    path('request/', views.requestleave),
    path('viewmyleaves/', views.Viewmyleaves),
    path('dashboard/', views.dashboard),
    path('payslips/',views.mypayslips),
    path('weeklyactivity/',views.weeklyactivity1),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)