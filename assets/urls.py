# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 10:58
# @Author  : Tianhao
# @Email   : xth9363@163.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from assets import views

app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
    path('', views.dashboard),
]
