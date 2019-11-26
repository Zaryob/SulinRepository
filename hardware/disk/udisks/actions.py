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
    #shelltools.system("gtkdocize --copy")
    #autotools.autoreconf("-ivf")
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
                        --localstatedir=/var \
                        --libexecdir=/usr/lib/udisks \
                        --disable-static \
                        --enable-lvm2 \
                        --disable-gtk-doc \
                        --disable-man-pages")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.move("%s/lib/udev"% get.installDIR(), "%s/usr/lib/udev"% get.installDIR())
    inarytools.removeDir("/lib")

    inarytools.dodoc("AUTHORS", "COPYING", "NEWS", "README.md")
