#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import patterns,  url 

import views

urlpatterns = patterns('',
    #url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
)
