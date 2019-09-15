#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod u+s,go-r /usr/bin/gpg2")
    os.system("/bin/chmod u+s,go-r /usr/bin/gpg-agent")
