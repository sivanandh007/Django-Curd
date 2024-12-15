from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('full_name','mobile','emp_code','position')
        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'Employee Code',
            'mobile' : 'Phone No',

        }
