"""
Add any additional URLs that should only be available when using the the
settings.development configuration.

See ``urls.defaults`` for a list of all URLs available across both
configurations.
"""
from .defaults import *
from django.conf import settings

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
urlpatterns += patterns('',

    # Examples:
    # url(r'^$', 'tutorial.views.debug', name='debug'),
    # url(r'^tutorial/', include('tutorial.debug.urls')),
)
