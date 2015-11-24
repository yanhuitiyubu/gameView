#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import patterns,  url 

import views

urlpatterns = patterns('',
    #url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news, name='news'),
    url(r'^schedule', views.schedule, name='schedule'),
    url(r'^basketball_info', views.basketball_info, name='basketball_info'),
    url(r'^football_info', views.basketball_info, name='football_info'),
    url(r'^football_rank', views.basketball_info, name='football_rank'),
    url(r'^basketball_rank', views.basketball_info, name='basketball_rank'),
)
