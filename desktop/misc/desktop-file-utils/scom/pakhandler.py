#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ciksemel
import os

def updateData(filepath):
    parse = ciksemel.parse(filepath)

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/share/applications"):
            os.system("/usr/bin/update-desktop-database -q")
            return

def setupPackage(metapath, filepath):
    updateData(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateData(filepath)
