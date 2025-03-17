from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentRegistrationForm,EditStudentRegistrationForm
# Create your views here.

def homepage(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_registration(request):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successfully! ')
            return redirect('homepage')
    else:
        form=StudentRegistrationForm()
    context={
        'form':form
    }
    return render(request,'registration.html',context)
    
def student_detail(request,pk):
    student=get_object_or_404(Student,pk=pk)
    context={
        'student':student
    }
    return render(request,'student_detail.html',context)

def edit_information(request,student_id):
    student=get_object_or_404(Student,pk=student_id)
    if request.method == "POST":
        form =EditStudentRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated Successfully!')
            return redirect('/')
    else:
        form=EditStudentRegistrationForm(instance=student)
        context={
            'form':form
        }
        return render(request,'registration.html',context)

def delete_information(request,student_id):
    student=get_object_or_404(Student,pk=student_id)
    student.delete()
    messages.success(request,'Student information deleted Successfully!')
    return redirect('/')