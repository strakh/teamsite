from django.conf.urls import patterns, include, url
from django.contrib import admin
from teamproject.views import main, employee, projects, article, employee_one

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	url(r'^main/',main, name='teamproject_main'),
	(r'^employee/$',employee),
	url(r'^employee/(\d{1,2})',employee_one, name='teamproject_employee_view'),
	(r'^projects/',projects),
	(r'^article/',article),
    # url(r'^$', 'teamproject.views.home', name='home'),
    # url(r'^teamproject/', include('teamproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
