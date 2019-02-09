# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def build():
    # NOTE: This is only for the start-stop-daemon
    autotools.make('CC="%s" LD="%s %s" CFLAGS="%s"' % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)
    inarytools.dodir("/tmp")
    inarytools.dodir("/tmp")
    inarytools.dodir("/var/tmp")
    inarytools.dodir("/run/shm")
    inarytools.dodir("/var/lock")

    # Adjust permissions
    chmod("/tmp", 0o777)
    chmod("/var/tmp", 0o777)
    chmod("/run/shm", 0o777)
    chmod("/var/lock", 0o775)

    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        inarytools.dodir("/lib32")
        inarytools.dodir("/usr/lib32")

        # Hack for binary blobs built on multi-lib systems
        inarytools.dosym("lib", "/lib64")

    inarytools.dosym("sulin-release", "/etc/system-release")
