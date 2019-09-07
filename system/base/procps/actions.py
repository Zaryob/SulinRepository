#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    inarytools.dosed("watch.c", "ncursesw/ncurses.h", "ncurses.h")
    
    autotools.configure("--prefix=/usr \
                         --exec-prefix=/ \
                         --disable-static \
                         --sysconfdir=/etc \
                         --libdir=/usr/lib \
                         --bindir=/usr/bin \
                         --sbindir=/usr/bin \
                         --enable-watch8bit \
                         --without-systemd")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('ln_f="ln -sf" ldconfig="true" lib64=lib DESTDIR=%s' % get.installDIR())
    
    #remove conflicts
    inarytools.remove("/usr/bin/kill")
    inarytools.remove("/usr/bin/pidof")
    inarytools.remove("/usr/share/man/man1/kill.1")
    inarytools.remove("/usr/share/man/man1/pidof.1")
    
    # for mudur and scom
    inarytools.dosym("../usr/bin/sysctl", "/sbin/sysctl")
    inarytools.dosym("../usr/bin/ps", "/bin/ps")

    #inarytools.dosym("libproc-%s.so" % get.srcVERSION(), "/lib/libproc.so")

    inarytools.dodoc("NEWS", "ps/HACKING")
