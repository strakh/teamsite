from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from teamdb.models import Employee, Article, Projects
from django.http import Http404
from teamproject.forms import Email
import os.path

def main(request):
    return render(request,'main.html',)

def employee(request):
    values = Employee.objects.order_by('name')
    return render(request,'employee.html',{'employee_list': values })

def article(request):
    #TODO: remove limits or use paginator
    values = Article.objects.order_by('title')[0:4]
    return render(request,'article.html',{'article_list': values })
    
def employee_one(request, offset):
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/search/?')
    else:
        try:
			offset = int(offset)
			value = Employee.objects.get(id = offset)
			url =  value.img.url
        except ValueError:
		    raise Http404()
        except Employee.DoesNotExist:
			raise Http404()        
        except AttributeError:
			url = os.path.join(os.path.dirname(__file__),'img/nobody.png').replace('\\','/')
        form = Email()
    return render(request,'employee_one.html',{'employee': value, 'url': url, 'form': form })

def projects(request):
    #(SOLVED)TODO: the same bug with exception as earlier
    try:
        values = Projects.objects.order_by('name')
        url =  values.img.url
    except Projects.DoesNotExist:
        #TODO: you still don't use this variable anywhere
        e_list = "No projects"
    except AttributeError:
		url = os.path.join(os.path.dirname(__file__),'img/nothing.png').replace('\\','/')
    return render(request,'projects.html',{'project_list': values,'url': url })

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        emp = Employee.objects.filter(name__icontains=q)
        return render(request,'search.html',
            {'emp': emp, 'query': q})
    else:
        values = Employee.objects.order_by('name')
        return render(request,'employee.html',{'employee_list': values }) 

#def article(request):
#    return render(request,'article.html',)

