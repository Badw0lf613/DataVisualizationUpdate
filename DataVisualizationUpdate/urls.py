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
    path('', views.main, name="main"),  # 主页面
    path('time', views.get_time, name="time"),  # 获取时间
    path('c1', views.get_c1_data, name="c1"),  # 获取c1
    path('c2', views.get_c2_data, name="c2"),  # 获取c2
    path('l1', views.get_l1_data, name="l1"),  # 获取l1
    path('l2', views.get_l2_data, name="l2"),  # 获取l2
    path('r1', views.get_r1_data, name="r1"),  # 获取r1
    path('r2', views.get_r2_data, name="r2"),  # 获取r2
    path('china', views.china, name="china"),  # 中国页面
    path('china/c1', views.get_c2_data_china, name="china/c1"),  # 获取c1
    path('china/c2', views.get_c2_data_china, name="china/c2"),  # 获取c2
    path('china/l1', views.get_l1_data_china, name="china/l1"),  # 获取l1
    path('china/l2', views.get_l2_data_china, name="china/l2"),  # 获取l2
    path('shanghai', views.shanghai, name="shanghai"),  # 上海页面
    # path('shanghai/c1', views.get_c1_data_shanghai, name="shanghai/c1"),  # 获取c1
    path('shanghai/c2', views.get_c2_data_shanghai, name="shanghai/c2"),  # 获取c2
    path('shanghai/l1', views.get_l1_data_shanghai, name="shanghai/l1"),  # 获取l1
    path('shanghai/l2', views.get_l2_data_shanghai, name="shanghai/l2"),  # 获取l2
    path('world', views.world, name="world"),  # 全球页面
]
