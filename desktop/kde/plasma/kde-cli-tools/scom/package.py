#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("ln -s /usr/lib/kf5/kdesu /usr/bin/kdesu") 
