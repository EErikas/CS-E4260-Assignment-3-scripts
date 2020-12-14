"""multimedia_assignment_3_serrver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', show_index, name='index'),
    path('janus-admin/', show_admin, name='janus-admin'),
    path('client/', show_client, name='client'),
    path('streamer/', show_streamer, name='streamer'),
    path('hls/rtp', show_rtp_to_hls, name='rtp_hls'),
    path('hls/rtmp', show_rtmp_to_hls, name='rtmp_hls'),
    path('start/ffmpeg', execute_command, name='run_ffmpeg'),
]
