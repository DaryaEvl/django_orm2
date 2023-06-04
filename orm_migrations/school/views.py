from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students_list = Student.objects.all().order_by('group')
    teachers_list = Teacher.objects.all()
    context = {'students_list': students_list, 'teachers_list': teachers_list}
    return render(request, template, context)
