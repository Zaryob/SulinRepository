# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("sh makeconf.sh")
    
    # Disable device node creation during build/install
    inarytools.dosed("util/Makefile.in", "mknod", "echo Disabled: mknod ")


    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-lib \
                         --enable-util \
                         --exec-prefix=/ \
                         --bindir=/bin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/dev")
    inarytools.removeDir("/etc")

    # Make compat symlinks into /usr/bin
    inarytools.dosym("/bin/fusermount", "/usr/bin/fusermount2")
    inarytools.dosym("/bin/ulockmgr_server", "/usr/bin/ulockmgr_server2")

    # Move pkgconfig file to /usr/lib
    inarytools.domove("/lib/pkgconfig", "/usr/lib/")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README.NFS")
