# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'FCAPJr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^$', include('FCAPJr.fcap_app.urls', namespace='fcap_app')),
    url(r'^send-email/', 'FCAPJr.fcap_app.views.enviar_email', name='send-email'),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)