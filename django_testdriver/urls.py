import os
from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings as django_testdriver_settings

urlpatterns = patterns('',
    url(r'^jasmine/$', 'django_testdriver.views.custom_spec_runner', name='custom_spec_runner'),

    (r'^test/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': django_testdriver_settings.MEDIA_ROOT }),

    url(r'^coverage/$', 'django_testdriver.views.coverage_view', name='coverage_view'),

    (r'^coverage/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(django_testdriver_settings.JSTESTDRIVER_OUTPUT, 'html') }),
)
