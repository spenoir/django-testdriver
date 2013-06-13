import os
from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings as djash_settings

urlpatterns = patterns('',
    url(r'^jasmine/$', 'django-testdriver.views.custom_spec_runner', name='custom_spec_runner'),

    (r'^test/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': djash_settings.MEDIA_ROOT }),

    url(r'^coverage/$', 'django-testdriver.views.coverage_view', name='coverage_view'),

    (r'^coverage/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(djash_settings.JSTESTDRIVER_OUTPUT, 'html') }),
)
