from django import forms
from Staff.models import *

class Staff_Form(forms.ModelForm):
    class Meta:
        model=STAFF_PERSONAL
        fields=["staff_name","staff_age","staff_contact","staff_email","staff_department"]
        label={
            'staff_name':'Staff Name',
            'staff_age':'Staff Age',
            'staff_contact':'Contact Number',
            'staff_email':'E-mail Address',
            'staff_department':'Department',
        }

        widgets={
            'staff_name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'staff_age':forms.TextInput(attrs={'placeholder':'Enter your Age'}),
            'staff_contact':forms.TextInput(attrs={'placeholder':'Enter your Contact Number'}),
            'staff_email':forms.EmailInput(attrs={'placeholder':'eg:abc@gmail.com'}),
            'staff_department':forms.Select(choices=Departments)

        }

