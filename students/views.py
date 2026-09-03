from django.shortcuts import render
from students.models import Student  
from students.forms import StudentForm 
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.serializers import StudentSerializer
# Create your views here.
@api_view(['GET'])
def student_list_api(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
def hello(request):
    students = Student.objects.all()
    return render(request, 'students/hello.html', {'students': students})

@login_required
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