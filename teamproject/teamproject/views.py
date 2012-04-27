from django.shortcuts import render_to_response
#import datetime
from teamdb.models import Employee

def main(request):
    return render_to_response('main.html',)

def employee(request):
    try:
        values = Employee.objects.order_by('name')[0:2]
    except Employee.DoesNotExist:
        e_list = "No employees" 
    return render_to_response('employee.html',{'employee_list': values })

def employee_one(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    value = Employee.objects.get(id = offset)
    name = value.name
    spec = value.specialization
    info = value.info
    try:
        url =  value.img.url
    except AttributeError:
		url = "/home/den/img/nobody.jpg"
    return render_to_response('employee_one.html',{'name': name, 'spec': spec,'info': info, 'url': url })

def projects(request):
    return render_to_response('projects.html',)

def article(request):
    return render_to_response('article.html',)

