"""DataVisualizationUpdate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cov import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),  # 主页面
    path('time', views.get_time, name="time"),  # 获取时间
    path('c1', views.get_c1_data, name="c1"),  # 获取时间
    path('c2', views.get_c2_data, name="c2"),  # 获取时间
    path('l1', views.get_l1_data, name="l1"),  # 获取时间
    path('l2', views.get_l2_data, name="l2"),  # 获取时间
    path('r1', views.get_r1_data, name="r1"),  # 获取时间
    path('r2', views.get_r2_data, name="r2"),  # 获取时间
]
