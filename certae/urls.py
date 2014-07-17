from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from certae.settings import PPATH

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^main$', TemplateView.as_view(template_name='index.html')),
    url(r'^debug$', TemplateView.as_view(template_name='rai-debug.html')),

    url(r'^protoDiagram/', include('dbDesigner.urls')),
    url(r'^rai/', include('rai.urls')),
    
    
    #    Use for production instalation and for load json configuration files
    url(r'static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PPATH + '/static'}),
    url(r'resources/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PPATH + '/static'}),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': PPATH + '/static'}),
    url(r'^', include('protoLib.urls')),

)