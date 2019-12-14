#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ciksemel
import os

def updateCaches(filepath):
    parse = ciksemel.parse(filepath)
    GIO_MODULE_PATH = "usr/lib32/gio/modules"

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith(GIO_MODULE_PATH):
            os.system("/usr/bin/32/gio-querymodules /%s" % GIO_MODULE_PATH)
            break

def setupPackage(metapath, filepath):
    updateCaches(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateCaches(filepath)
