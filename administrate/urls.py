#!/usr/bin/env python
# encoding: utf-8
"""
    @author: Magic Joey
    @contact: outlierw@gmail.com
    @site: http://underestimated.me
    @project: metamall_service
    @description:
    @version: 2016-05-12 21:26,urls V1.0 
"""
from django.conf.urls import patterns, url
from administrate import views

urlpatterns = patterns(
    url(r'^', views.index),
)
