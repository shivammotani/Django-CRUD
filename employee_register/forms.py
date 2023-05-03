from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Code',
            'mobile': 'Mobile Number'
        }

    def __init__(self,*args, **kwargs):
        super(forms.ModelForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Choose a postion from the dropdown'
        self.fields['emp_code'].required = False