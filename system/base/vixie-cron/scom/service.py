from scom.service import *

serviceType = "local"
serviceDesc = {"en": "Cron Task Scheduler",
                 "tr": "Cron Görev Zamanayici" }
serviceDefault = "on"

@synchronized
def start():
    startService(command="/usr/sbin/cron",
                 pidfile="/var/run/cron.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/cron.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/cron.pid")
