from django_hosts import patterns, host
from . import settings

host_patterns =
    patterns(
        '',
        host('banqueting.condivision.cloud:8000', 'banqueting.urls', name='primo'),
        host('127.0.0.1:8000', 'condivision.urls', name='127.0.0.1'),
		host('calderoni.condivision.cloud:8000', 'banqueting.calderoni.urls', name='company.com'),
		host(r'api', 'api.urls', name='api'),
		host(r'beta', 'beta.urls', name='beta'),
    )
