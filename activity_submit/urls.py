# -*- coding:utf-8 -*-
# @Author: syz
# @Time: 2022/11/10 16:57
# @File: urls.py
from django.urls import path, re_path
from django.conf import settings
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf.urls.static import static

from . import views

# app_name = 'activity_submit'

# handler404 = views.page_not_found
urlpatterns = [
                  # 主页url
                  path('', views.index, name='index'),
                  path('submit_form/<teammate>', views.submit_form, name='submit_form'),
                  path('ajax_get', views.ajax_get, name='ajax_get'),

                  # 定义图片url
                  re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
