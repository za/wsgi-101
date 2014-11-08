#!/usr/bin/python

import views

urls = [
    (r'^$', views.index),
    (r'hello/?$', views.hello),
    (r'hello/(.+)$', views.hello),
]
