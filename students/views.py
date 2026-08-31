from django.http import HttpResponse
from students.models import Student   
# Create your views here.
def hello(request):
    students = Student.objects.all() 
    return HttpResponse(students)