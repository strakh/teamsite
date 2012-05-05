from django.conf.urls import patterns, include, url
from django.contrib import admin
from teamproject.views import main, employee, projects, article, employee_one, search

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	#TODO: make mail page root
	url(r'^main/$',main, name='teamproject_main'),
	url(r'^employee/$',employee, name='teamproject_employee'),
	url(r'^employee/(\d{1,2})',employee_one, name='teamproject_employee_view'),
	url(r'^projects/$',projects, name='teamproject_projects'),
	url(r'^article/$',article, name='teamproject_article'),
	#url(r'^search-form/$', search_form, nameen/employee/='teamproject_search-form'),
    url(r'^search/$', search, name='teamproject_search'),
    # url(r'^$', 'teamproject.views.home', name='home'),
    # url(r'^teamproject/', include('teamproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
