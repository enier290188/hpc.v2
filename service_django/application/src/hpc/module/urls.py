# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^hpc/', include('src.hpc.module.hpc.urls', namespace='hpc')),
]
