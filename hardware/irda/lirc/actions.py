#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

#WorkDir = "lirc-%s" % get.srcVERSION().replace("_", "-")

def setup():
    autotools.configure("--localstatedir=/var \
                         --enable-sandboxed \
                         --with-systemdsystemunitdir=no \
                         --enable-shared \
                         --disable-static \
                         --disable-debug \
                         --disable-dependency-tracking \
                         --with-transmitter \
                         --with-x \
                         --with-driver=userspace \
                         --with-syslog=LOG_DAEMON")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dobin("contrib/irman2lirc")

    
    # example configs
    inarytools.insinto("/etc", "contrib/lircd.conf", "lircd.conf")
    inarytools.insinto("/etc", "contrib/lircmd.conf", "lircmd.conf")

    inarytools.dohtml("doc/html/*.html")
    inarytools.rename("/%s/%s" % (get.docDIR(), get.srcNAME()), "lirc")

    inarytools.insinto("/%s/lirc/contrib" % get.docDIR(), "contrib/*")
    inarytools.insinto("/lib/udev/rules.d", "contrib/*.rules", "60-lirc.rules")
    inarytools.remove("/var/run/lirc")

