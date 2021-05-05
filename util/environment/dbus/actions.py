#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
env=os.environ.copy()
from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    #inarytools.dosed("configure.ac", '(AS_AC_EXPAND\(EXPANDED_LOCALSTATEDIR, )"\$localstatedir"\)', r'\1 "")')
    #for f in ["bus/Makefile.am", "bus/Makefile.in"]:
    #    inarytools.dosed(f, "\$\(localstatedir\)(\/run\/dbus)", "\\1")
    options = "PYTHON=/usr/bin/python3 \
               --disable-selinux \
               --with-xml=expat \
		       --with-dbus-user=messagebus \
		       --with-system-pid-file=/var/run/dbus.pid \
		       --disable-verbose-mode \
		       --disable-static \
		       --enable-inotify \
		       --disable-dnotify \
		       --enable-modular-tests=yes \
		       --disable-asserts \
		       --enable-user-session \
		       --disable-xml-docs \
		       --with-session-socket-dir=/tmp \
		       --with-x"


    if get.buildTYPE() == "emul32":
        os.environ.clear()
        os.environ.update(env)
        shelltools.export("CC", "gcc -m32 -mstackrealign")
        shelltools.export("CXX", "g++ -m32 -mstackrealign")
        shelltools.export("HOST", "x86_64")
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += "\
                    --libdir=/usr/lib32 \
                    --disable-doxygen-docs"

    autotools.autogen()
    autotools.configure(options)

def build():
    autotools.make()

def check():
    pass
    #FIXME: uid test failed because of fakeroot environment
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    # needs to exist for the system socket
    inarytools.dodir("/var/run/dbus")
    inarytools.dodir("/var/lib/dbus")
    inarytools.dodir("/usr/share/dbus-1/services")
    os.system("/bin/chown root:dbus {}/usr/libexec/dbus-daemon-launch-helper".format(get.installDIR()))
    os.system("/bin/chmod -v 4750 {}/usr/libexec/dbus-daemon-launch-helper".format(get.installDIR()))
    inarytools.dohtml("doc/")
