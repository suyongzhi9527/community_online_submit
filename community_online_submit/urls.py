"""community_online_submit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

favicon_view = RedirectView.as_view(url='/static/form_1/img/favicon.ico', permanent=True)  # django2.2

# 修改后台站点头部和标题
admin.site.site_title = '社区活动报名后台管理系统'  # 站点标题
admin.site.site_header = '社区活动报名后台管理系统'  # 站点头部

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('activity_submit/', include('activity_submit.urls')),
                  path('', include('submit.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
