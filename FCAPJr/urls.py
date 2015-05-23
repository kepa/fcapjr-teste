# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'FCAPJr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^$', include('FCAPJr.fcap_app.urls', namespace='fcap_app')),
    url(r'^admin/', include(admin.site.urls)),
)
