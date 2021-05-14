#!/usr/bin/python3
import os

def postInstall():
    os.system("chmod u+s /usr/bin/fusermount")
