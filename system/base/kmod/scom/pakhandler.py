# -*- coding: utf-8 -*-

import inary.sxml.xmlext as xmlext
import subprocess

def domodules(filepath):
    doc = xmlext.parse(filepath)
    for item in xmlext.getAllNodes("File"):
        path = xmlext.getNodeText(item,"Path")
        if path.startswith("lib/modules/"):
            kernelVersion = path.split("/")[2]
            subprocess.call(["/sbin/depmod", "-a", kernelVersion])
            return

def setupPackage(metapath, filepath):
    domodules(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    domodules(filepath)
