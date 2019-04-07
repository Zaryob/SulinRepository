#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inary.sxml.xmlext as xmlext 
import os

def updateCaches(filepath):
    parse = xmlext.parse(filepath)
    GIO_MODULE_PATH = "usr/lib32/gio/modules"
    GSCHEMAS_MODULE_PATH = "usr/share/glib-2.0/schemas"

    for icon in xmlext.getAllNodes(parse,"File"):
        path = xmlext.getNodeText(icon,"Path")
        if path.startswith(GIO_MODULE_PATH):
            os.system("/usr/bin/32/gio-querymodules /%s" % GIO_MODULE_PATH)
            break

    for icon in xmlext.getAllNodes(parse,"File"):
        path = xmlext.getNodeText(icon,"Path")
        if path.startswith(GSCHEMAS_MODULE_PATH):
            os.system("/usr/bin/glib-compile-schemas /%s" % GSCHEMAS_MODULE_PATH)
            return

def setupPackage(metapath, filepath):
    updateCaches(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateCaches(filepath)
