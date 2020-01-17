#!/usr/bin/env python3
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = {"en": "Nginx Web Server",
               "tr": "Nginx Web Sunucusu"}

from scom.service import *

@synchronized
def start():
    startService(command="/usr/sbin/nginx",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/nginx.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/nginx.pid")
