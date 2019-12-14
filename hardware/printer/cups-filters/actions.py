# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    inarytools.dosed("configure", "localstatedir/run/cups", "localstatedir/cups")
    shelltools.system("./autogen.sh")
    autotools.configure("--sbindir=/usr/bin \
                         --localstatedir=/var \
                         --enable-dbus \
                         --with-rcdir=no \
                         --disable-static \
                         --with-gs-path=/usr/bin/gs \
                         --with-pdftops-path=/usr/bin/gs \
                         --docdir=/usr/share/doc/cups-filters-1.0.76 \
                         --with-browseremoteprotocols=DNSSD,CUPS ")

    #inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("check")
    
#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
