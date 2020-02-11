#!/usr/bin/env python3

import os

def postInstall():
    os.system("/usr/sbin/update-ca-certificates --fresh")

def postRemove():
    pass
    
def preRemove():
    pass
