from django.conf.urls import patterns, include, url
from django.contrib import admin
#from teamproject.views import main, employee, projects, article, employee_one, search
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	#(SOLVED)TODO: make mail page root
)
urlpatterns += patterns('teamproject.views',
	url(r'^main/$','main', name='teamproject_main'),
	url(r'^employee/$','employee', name='teamproject_employee'),
	url(r'^employee/(?P<offset>\d{1,2})','employee_one', name='teamproject_employee_view'),
	url(r'^projects/$','projects', name='teamproject_projects'),
	url(r'^article/$','article', name='teamproject_article'),
	#url(r'^search-form/$', search_form, nameen/employee/='teamproject_search-form'),
    url(r'^search/$', 'search', name='teamproject_search'),
    url(r'^$', 'search', name='home'),
    # url(r'^teamproject/', include('teamproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
