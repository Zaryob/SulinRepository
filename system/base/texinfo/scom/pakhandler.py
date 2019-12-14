# -*- coding: utf-8 -*-

import os
import inary.sxml.xmlext as xmlext
import subprocess

def doinfo(filepath, remove=False):
    # install-info is broken with i18n :(
    os.environ["LC_ALL"] = "C"

    doc = xmlext.parse(filepath)
    for item in xmlext.getAllNodes(doc, "File"):
        path = xmlext.getNodeText(item, "Path")
        if path.startswith("usr/share/info") and path.endswith((".info", ".info.gz")):
            if remove:
                subprocess.call(["install-info", "--delete", "/%s" % path, "/usr/share/info/dir"])
            else:
                subprocess.call(["install-info", "/%s" % path, "/usr/share/info/dir"])

def setupPackage(metapath, filepath):
    doinfo(filepath)

def cleanupPackage(metapath, filepath):
    doinfo(filepath, True)

def postCleanupPackage(metapath, filepath):
    pass
