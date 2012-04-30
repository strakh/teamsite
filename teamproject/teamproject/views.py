#TODO: learn the difference between render and render_to_response functions
# and make a proper decision
from django.shortcuts import render_to_response
from teamdb.models import Employee, Article, Projects
import os.path

def main(request):
    return render_to_response('main.html',)

def employee(request):
    #(SOLVED)TODO: Are you sure you can get an exception here?
    #try:
    values = Employee.objects.order_by('name')
    #except Employee.DoesNotExist:
        #(SOLVED)TODO: Why do you need this? you never use it later.
        #e_list = "No employees" 
    return render_to_response('employee.html',{'employee_list': values })

def article(request):
    #try:
    values = Article.objects.order_by('title')[0:4]
    #except Article.DoesNotExist:
        #e_list = "No articles" 
    return render_to_response('article.html',{'article_list': values })
    
def employee_one(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    #(SOLVED)TODO: What about exceptions here?
    try:
        value = Employee.objects.get(id = offset)
    except ValueError:
        raise Http404()
    #(SOLVED)TODO: It's better to pass the whole value object to template, isn't it?
    #name = value.name
    #spec = value.specialization
    #info = value.info
    try:
        url =  value.img.url
    except AttributeError:
		url = os.path.join(os.path.dirname(__file__),'img/nobody.png').replace('\\','/')
    return render_to_response('employee_one.html',{'employee': value, 'url': url })

def projects(request):
    try:
        values = Projects.objects.order_by('name')
    except Projects.DoesNotExist:
        e_list = "No projects" 
    try:
        url =  values.img.url
    except AttributeError:
		url = os.path.join(os.path.dirname(__file__),'img/nothing.png').replace('\\','/')
    return render_to_response('projects.html',{'project_list': values,'url': url })

#def article(request):
#    return render_to_response('article.html',)

