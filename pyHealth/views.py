from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Employee

def index(request):
    template = loader.get_template(('index.html'))
    return HttpResponse(template.render())

def employee_data(request):
    employee_objects = Employee.objects.all().values()

    template = loader.get_template(('employee_data.html'))
    context = {
        'employee_objects': employee_objects,
    }
    return HttpResponse(template.render(context, request))



