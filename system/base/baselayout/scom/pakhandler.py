# -*- coding: utf-8 -*-

def update_ld_so_cache(filepath):
    import glob
    import inary.sxml.xmlext as xmlext
    import subprocess

    libdirs = []

    for config_file in glob.glob("/etc/ld.so.conf.d/*.conf"):
        for line in open(config_file):
            line = line.strip()
            if line.startswith("/"):
                libdirs.append(line[1:])

    libdirs = tuple(libdirs)

    doc = xmlext.parse(filepath)
    for item in xmlext.getAllNodes(doc, "File"):
        path = xmlext.getNodeText(item,"Path")
        if path.startswith(libdirs):
            subprocess.call(["/sbin/ldconfig", "-X"])
            return

def setupPackage(metapath, filepath):
    update_ld_so_cache(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    update_ld_so_cache(filepath)
