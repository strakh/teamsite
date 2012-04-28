#TODO: learn the difference between render and render_to_response functions
# and make a proper decision
from django.shortcuts import render_to_response
#import datetime
from teamdb.models import Employee, Article, Projects

def main(request):
    return render_to_response('main.html',)

def employee(request):
    #TODO: Are you sure you can get an exception here?
    try:
        values = Employee.objects.order_by('name')[0:2]
    except Employee.DoesNotExist:
        #TODO: Why do you need this? you never use it later.
        e_list = "No employees" 
    return render_to_response('employee.html',{'employee_list': values })

def article(request):
    try:
        values = Article.objects.order_by('title')[0:2]
    except Article.DoesNotExist:
        e_list = "No articles" 
    return render_to_response('article.html',{'article_list': values })
    
def employee_one(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    #TODO: What about exceptions here?
    value = Employee.objects.get(id = offset)
    #TODO: It's better to pass the whole value object to template, isn't it?
    name = value.name
    spec = value.specialization
    info = value.info
    try:
        url =  value.img.url
    except AttributeError:
		url = "/home/den/img/nobody.jpg"
    return render_to_response('employee_one.html',{'name': name, 'spec': spec,'info': info, 'url': url })

def projects(request):
    try:
        values = Projects.objects.order_by('name')[0:2]
    except Projects.DoesNotExist:
        e_list = "No projects" 
    return render_to_response('projects.html',{'project_list': values })

#def article(request):
#    return render_to_response('article.html',)

