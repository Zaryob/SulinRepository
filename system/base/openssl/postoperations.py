#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def postInstall():
    os.system("/usr/bin/c_rehash /etc/ssl/certs")

def postRemove():
    pass
    
def preRemove():
    pass
