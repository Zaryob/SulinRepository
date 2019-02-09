#!/usr/bin/python
# -*- coding: utf-8 -*-

from scom.service import *
import time


serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Remote Filesystem Mounter",
                 "tr": "Uzak Dosyasistemi Bağlayıcı"})

DATAFILE = "/var/run/netfs.status"

MSG_NM_NOT_RUNNING = _({"en": "NetworkManager service is not running",
                        "tr": "NetworkManager hizmeti çalışmıyor",
                       })

@synchronized
def start():
    # Mount all remote filesystems
    if run("/usr/bin/nm-online -q -t 10") != 0:
        # NM is not running
        fail(MSG_NM_NOT_RUNNING)

    fstab = Fstab()
    for entry in fstab.get_entries():
        if entry.is_remote_mount():
            if entry.is_nfs():
                # Start rpcbind if fs is nfs|nfs4
                startDependencies("rpcbind")
            # Mount it
            entry.mount()

@synchronized
def stop():
    # Unmount all remote filesystems
    pass
    
def status():
    pass
