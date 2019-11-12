# -*- coding: utf-8 -*-
from scom.service import *

serviceType = "server"
serviceDesc = {"en": "Slurpd Daemon",
               "tr": "Slurpd Servisi"}

def start():
    startService(command="/usr/libexec/slurpd",
                 donotify=True)

def stop():
    stopService(command="/usr/libexec/slurpd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/libexec/slurpd")
