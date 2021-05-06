#!/usr/bin/env python3

import os

def postInstall():
    os.system("/bin/chown root:mail /etc/sasl2/sasldb2")
    os.system("/bin/chmod 0640 /etc/sasl2/sasldb2")
