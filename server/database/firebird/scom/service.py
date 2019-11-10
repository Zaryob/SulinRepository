#!/usr/bin/env python3
# -*- coding: utf-8 -*-

serviceType="server"
serviceDesc = {"en": "Firebird Database Server",
               "tr": "Firebird Veritabanı Sunucusu"}

from scom.service import *

pid_file = "/run/firebird/firebird.pid"

@synchronized
def start():
    startService(command="/opt/firebird/bin/fbguard",
                 args="-pidfile %s -start -forever -daemon" % pid_file,
                 pidfile="/run/firebird/firebird.pid",
                 donotify=True)
#                 chuid="firebird",

@synchronized
def stop():
    stopService(pidfile=pid_file,
                donotify=True)

def status():
    return isServiceRunning(pid_file)
