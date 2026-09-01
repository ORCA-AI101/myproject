from django.shortcuts import render
from students.models import Student  
from students.forms import StudentForm 
# Create your views here.
def hello(request):
    students = Student.objects.all()
    return render(request, 'students/hello.html', {'students': students})
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                name=form.cleaned_data['name'],
                grade=form.cleaned_data['grade']
            )
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})