import socket
from django.shortcuts import render, redirect


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
        "source_url": "http://192.168.1.125:8080/live/testRTP.m3u8"
    })


def show_rtmp_to_hls(request):
    return render(request, 'hls.html', context={
        "name": "RTMP to HLS (From OBS)",
        "source_url": "http://192.168.1.125:8080/live/testRTMP.m3u8"
    })
