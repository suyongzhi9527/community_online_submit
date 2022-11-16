# -*- coding:utf-8 -*-
# @Author: syz
# @Time: 2022/11/11 13:52
# @File: urls.py
from django.urls.conf import path
from . import views

app_name = 'submit'

urlpatterns = [
    path('', views.new_person_request, name='new_person_request'),
    path('submit/<name>/<class_num>/<phone>/<qq_num>/<department>/', views.submit),
    path('new_person_request/', views.new_person_request, name='new_person_request'),
    path('new_person_submit/', views.new_person_submit, name='new_person'),
    path('community_person_request/', views.community_person_request, name='community_person_request'),
    path('community_person_submit/', views.community_person_submit, name='community_person_submit'),
]
