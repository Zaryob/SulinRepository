#!/usr/bin/python3
import os

def postInstall():
    os.system("groupadd --system openvpn 2>/dev/null")
    os.system("useradd --system -g openvpn -s /sbin/nologin openvpn")
