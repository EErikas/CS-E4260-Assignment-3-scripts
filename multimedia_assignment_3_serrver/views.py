import socket
import os
from django.shortcuts import render, HttpResponse, redirect
from .settings import BASE_DIR as base_dir


def show_index(request):
    return render(request, 'index.html')


def show_admin(request):
    return render(request, 'admin.html')


def show_client(request):
    return render(request, 'client.html')


def show_streamer(request):
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return render(request, 'streamer.html', context={"host_ip": local_ip})


def show_rtp_to_hls(request):
    return render(request, 'hls.html', context={
        "name": "RTP to HLS (From Janus)",
        "source_url": "http://localhost:8080/hls/test.m3u8"
    })


def execute_command(request):
    source_path = os.path.join(base_dir, 'source.sdp')
    command = 'ffmpeg -analyzeduration 450M -probesize 450M -protocol_whitelist file,udp,rtp -i {} -c:v libx264 -preset ultrafast -tune zerolatency -f flv rtmp://localhost/live/test'.format(
        source_path)
    os.popen(command)
    return HttpResponse('Executed:\n{}'.format(command))


def show_rtmp_to_hls(request):
    return render(request, 'hls.html', context={
        "name": "RTMP to HLS (From OBS)",
        "source_url": "http://localhost:8080/hls/testRTMP.m3u8"
    })
