from django_hosts import patterns, host
from . import  settings

host_patterns = patterns('',
    host('127.0.0.1', 'banqueting.urls', name='127.0.0.1'),
    host('company.com:8000', 'banqueting.calderoni.urls', name='company.com'),
    host(r'api', 'api.urls', name='api'),
    host(r'beta', 'beta.urls', name='beta'),
)
