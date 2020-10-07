#!/usr/bin/env python3

import os
import grp
import pwd
import shutil

def postInstall():
    try:
        os.system("rc-update add dbus default nonetwork")
        os.system("rc-update add elogind default nonetwork")
        os.system("rc-update add udev default nonetwork")
        os.system("rc-update add udev-settle default nonetwork")
        os.system("rc-update add udev-trigger default nonetwork")
        os.system("rc-update add kmod boot")
        os.system("rc-update add busybox-klogd default")
        os.system("rc-update add busybox-ntpd default")
        os.system("rc-update add busybox-syslogd default")
        os.system("rc-update add busybox-watchdog default")
        os.system("rc-update add opentmpfiles-dev boot default nonetwork")
        os.system("rc-update add opentmpfiles-setup boot default nonetwork")
    except: pass


def postRemove():
    pass

def preRemove():
    pass
