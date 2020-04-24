#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    inarytools.dosed("configure.ac", '(AS_AC_EXPAND\(EXPANDED_LOCALSTATEDIR, )"\$localstatedir"\)', r'\1 "")')
    for f in ["bus/Makefile.am", "bus/Makefile.in"]:
        inarytools.dosed(f, "\$\(localstatedir\)(\/run\/dbus)", "\\1")
    options = "PYTHON=/usr/bin/python3 \
               --disable-selinux \
               --disable-static \
               --disable-tests \
               --disable-asserts \
               --disable-checks \
               --disable-embedded-tests \
               --disable-modular-tests \
               --disable-doxygen-docs \
               --disable-systemd \
               --disable-libaudit \
               --disable-silent-rules \
               --enable-inotify \
               --enable-user-session \
               --with-xml=expat \
               --with-system-pid-file=/var/run/dbus/pid \
               --with-system-socket=/var/run/dbus/system_bus_socket \
               --with-console-auth-dir=/var/run/console/ \
               --with-session-socket-dir=/tmp \
               --with-dbus-user=dbus \
               --enable-abstract-sockets=auto \
               --disable-xml-docs"

    if get.buildTYPE() == "emul32":
        options += "\
                    --disable-xml-docs \
                    --libdir=/usr/lib32 \
                    --disable-doxygen-docs"

    autotools.autoreconf("-vif")
    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

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
