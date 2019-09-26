#!/usr/bin/env python3

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("groupadd -r -g 84 avahi")
    os.system("useradd -r -u 84 -g avahi -d / -s /bin/nologin -c avahi avahi")

    