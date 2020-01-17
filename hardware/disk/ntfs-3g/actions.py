#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.configure("--prefix=/usr \
                        --sbin=/usr/bin \
                        --mandir=/usr/share/man \
                        --disable-ldconfig \
                        --disable-static \
                        --with-fuse=external \
                        --enable-posix-acls \
                        --enable-ldscript \
                        --enable-extras")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s rootbindir=/usr/bin rootsbindir=/usr/bin rootlibdir=/usr/lib" % get.installDIR())

    inarytools.domove("/usr/bin/ntfs-3g.*", "/bin")

    # Create some compat symlinks
    inarytools.dosym("/usr/bin/ntfs-3g", "/sbin/mount.ntfs")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "CREDITS", "NEWS", "README")
    inarytools.dosym("/usr/share/doc/ntfs-3g", "/usr/share/doc/ntfsprogs")
