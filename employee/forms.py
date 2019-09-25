from django import forms
from .models import emp_experience

class experienceForm(forms.ModelForm):
    class Meta:
        model=emp_experience
        fields=['emp_org','emp_position' ,'emp_period' ,'emp_salary' ,'employee']

