#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/build-docbook-catalog")
