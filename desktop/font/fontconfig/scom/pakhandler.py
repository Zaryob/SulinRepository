# -*- coding: utf-8 -*-

import ciksemel
import subprocess

def updateCache(filepath):
    doc = ciksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("usr/share/fonts"):
            subprocess.call(["/usr/bin/fc-cache"])
            return

def setupPackage(metapath, filepath):
    updateCache(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateCache(filepath)
