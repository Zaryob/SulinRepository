#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ciksemel
import os

def updateData(filepath):
    parse = ciksemel.parse(filepath)

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders"):
            os.system("/usr/bin/gdk-pixbuf-query-loaders-32 --update-cache")
            return

def setupPackage(metapath, filepath):
    updateData(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateData(filepath)
