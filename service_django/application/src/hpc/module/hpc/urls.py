# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^module01/', include('src.hpc.module.hpc.module01.urls', namespace='module01')),
    url(r'^module02/', include('src.hpc.module.hpc.module02.urls', namespace='module02')),
    url(r'^module03/', include('src.hpc.module.hpc.module03.urls', namespace='module03')),
]
