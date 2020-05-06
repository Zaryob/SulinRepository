#!/usr/bin/env python3

import os

def postInstall():
    os.system("addgroup -S polkitd 2>/dev/null")
    os.system("adduser -S -D -H -h /var/empty -s /sbin/nologin -G polkitd -g polkitd polkitd 2>/dev/null")

def postRemove():
    pass
    
def preRemove():
    pass
