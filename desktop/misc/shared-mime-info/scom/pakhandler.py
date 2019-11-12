#!/usr/bin/env python3

import ciksemel
import os

def updateMimeTypes(filepath):
    parse = ciksemel.parse(filepath)
    paths = set()
    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if "/share/mime/packages/" in path and path.endswith(".xml"):
            paths.add("/%s" % path.partition("packages/")[0])

    for p in paths:
        os.system("/usr/bin/update-mime-database %s" % p)

def setupPackage(metapath, filepath):
    updateMimeTypes(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateMimeTypes(filepath)
