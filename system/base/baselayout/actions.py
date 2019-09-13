# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="."

def install():
    for i in {"/bin", "/sbin", "/lib", "/lib32", 
              "/etc", "/media", "/boot", "/mnt", "/opt",
              "/tmp", "/var/tmp", "/var/lock", "/usr", "/usr/bin",
              "/usr/lib", "/usr/lib32", "/usr/share", 
              "/run", "/run/shm",
              "/usr/local", "/usr/local/bin", "/usr/local/lib",
              "/usr/local/lib32"}:
        inarytools.dodir(i)

    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))
    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)

# Adjust permissions
    chmod("/tmp", 0o1777)
    chmod("/var/tmp", 0o1777)
    chmod("/run/shm", 0o1777)
    chmod("/var/lock", 0o775)
    chmod("/usr/share/baselayout/shadow", 0o600)

    inarytools.dosym("/run","/var/run")
    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        inarytools.dodir("/lib32")
        inarytools.dodir("/usr/lib32")

        # Hack for binary blobs built on multi-lib systems
        inarytools.dosym("lib", "/lib64")

    inarytools.dosym("sulin-release", "/etc/system-release")
