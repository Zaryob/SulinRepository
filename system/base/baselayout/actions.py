# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def install():
    for i in {"/bin", "/sbin", "/lib", "/lib32",
              "/etc", "/boot", "/mnt", "/opt",
              "/tmp", "/var/tmp", "/var/lock", "/usr", "/usr/bin",
              "/usr/lib", "/usr/lib32", "/usr/libexec", "/usr/share",
              "/run","/run/shm",
              "/usr/local", "/usr/local/bin", "/usr/local/lib", "/usr/local/libexec",
              "/usr/local/lib32"}:
        inarytools.dodir(i)

    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

# Adjust permissions
    shelltools.chmod("{}/tmp".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/var/tmp".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/run/shm".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/var/lock".format(get.installDIR()), 0o775)
    shelltools.chmod("{}/usr/share/baselayout/shadow".format(get.installDIR()), 0o600)
    inarytools.dosym("/run", "{}/var/run".format(get.installDIR()))

    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        inarytools.dodir("/lib32")
        inarytools.dodir("/usr/lib32")

        # Hack for binary blobs built on multi-lib systems
        inarytools.dosym("lib", "/lib64")

