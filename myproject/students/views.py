from django.shortcuts import render,redirect,get_object_or_404
from .models import Students
from django.http import HttpResponse

def student_list(request):
    students=Students.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_create(request):
    if request.method == 'POST':
        fName = request.POST['first_name']
        lName = request.POST['last_name']
        email  = request.POST['email']
        ph_no = request.POST['phone_number']
        dob = request.POST['date_of_birth']


        Students.objects.create(
            first_name=fName,
            last_name=lName,
            email = email,
            phone_number=ph_no,
            date_of_birth=dob,             
        )
        return redirect('student_list')
    return render(request,'student_form.html')

def student_update(request,id):
    std = get_object_or_404(Students,id=id)
    if request.method == 'POST':
        std.first_name = request.POST['first_name']
        std.last_name = request.POST['last_name']
        std.email  = request.POST['email']
        std.phone_number = request.POST['phone_number']
        std.date_of_birth = request.POST['date_of_birth']
        std.save()
        return redirect('student_list')
    return render(request,'student_form.html',{'student':std})
# Create your views here.
def student(request):
    return render(request,'portfolio.html')
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def profile(request):
    return render(request,'profile.html')




