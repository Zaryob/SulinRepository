#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/lib/inary/package"):
        os.system("mkdir /var/lib/inary/package")
        os.system("mv /var/lib/inary/* /var/lib/inary/package/")
        os.system("mv /var/lib/inary/package/scripts /var/lib/inary/")
def preRemove():
    pass
def preRemove():
    pass
