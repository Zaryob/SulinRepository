#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 722 /home/ftp/incoming")
    os.system("/bin/chown ftp:ftp /home/ftp/incoming -R")

def preRemove():
    pass

def postRemove():
    pass
