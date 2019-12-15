#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas >/dev/null 2>&1")


