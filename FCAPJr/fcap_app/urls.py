# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'FCAPJr.views.home', name='home'),
    'FCAPJr.fcap_app.views',
    url(r'^$', 'home', name='home'),
)


