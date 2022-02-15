from django.db import models

# Create your models here.

Departments=(
    ('ComputerScience','CSE'),
    ('Electrical','ECE'),
    ('Mechanical','MECH'),
    ('BioTechnology','BIOTECH')
)

class STAFF_PERSONAL(models.Model):
    staff_name=models.CharField(max_length=30)
    staff_age=models.IntegerField()
    staff_contact=models.CharField(max_length=10)
    staff_email=models.EmailField(max_length=30)
    staff_department=models.CharField(choices=Departments,max_length=30)

    class Meta:
        ordering=('-staff_age',)