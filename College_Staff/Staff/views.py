from django.shortcuts import redirect, render

from Staff.models import *
from Staff.forms import *

# Create your views here.

def HomePage(request):
    return render(request,'Staff/home.html')



def StaffDetails(request):
    details=STAFF_PERSONAL.objects.all()
    return render(request,'Staff/details.html',{'details':details})


def StaffForm(request):
    if request.method =="POST":
        form=Staff_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff_details")
    else:
        form = Staff_Form()
        return render(request,'Staff/staffForm.html',{'form':form})

def DeleteStaff(request,id):
    details=STAFF_PERSONAL.objects.get(id=id)
    details.delete()
    return redirect("staff_details")

def UpdateStaff(request,id):
    details=STAFF_PERSONAL.objects.get(id=id)
    if request.method =="POST":
        form = Staff_Form(request.POST,instance=details)
        if form.is_valid():
            form.save()
        return redirect("staff_details")
    else:
        return render(request,'Staff/updateForm.html',{'details':details})

def SearchForm(request):
    if 'staff_name' in request.GET:
        name = request.GET['staff_name']
        depart = request.GET['staff_department']
        result = STAFF_PERSONAL.objects.filter(staff_name__icontains=name).filter(staff_department__icontains=depart)
        return render(request,'Staff/searchStaff.html',{'result':result})
    else:
        return render(request,'Staff/searchStaff.html')


    