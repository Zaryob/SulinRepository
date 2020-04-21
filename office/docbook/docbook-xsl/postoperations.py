#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/build-docbook-catalog 2>/dev/null")
def preRemove():
    pass
def postRemove():
    pass
