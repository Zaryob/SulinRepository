#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.spawnle(os.P_WAIT, "/usr/bin/fc-cache", "/usr/bin/fc-cache", "-r", { "HOME": "/root/" })
