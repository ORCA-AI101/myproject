from django.shortcuts import render
from students.models import Student   
# Create your views here.
def hello(request):
    students = Student.objects.all()
    return render(request, 'students/hello.html', {'students':students})