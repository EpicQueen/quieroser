from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quieroser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tracks.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(BASE_DIR, 'media')}),

        # url(r'^__debug__/', include(debug_toolbar.urls)),
    )
