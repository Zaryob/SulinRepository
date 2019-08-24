#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/c_rehash /etc/ssl/certs")
