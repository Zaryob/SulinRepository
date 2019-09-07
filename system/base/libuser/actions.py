#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")

    autotools.configure("PYTHON={} \
                         --with-python \
                         --without-ldap \
                         --without-sasl \
                         --with-popt \
                         --disable-rpath \
                         --enable-gtk-doc-html=no \
                         --disable-gtk-doc".format(
                         "python2" if get.buildTYPE()=="rebuild_python" else "python3"))

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    shelltools.system("sed -i 's/SUBDIRS = po docs/SUBDIRS = po/' Makefile")

def build():
    autotools.make()

    autotools.make("-C po update-gmo")

def install():
    if get.buildTYPE()=="rebuild_python":
        autotools.rawInstall("DESTDIR='%s/python2'" % get.installDIR())
        shelltools.move("%s/python2/usr/lib/python2.7" % get.installDIR(),
                        "%s/usr/lib/" % get.installDIR())
        shelltools.unlinkDir("%s/python2" % get.installDIR())
        return

    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())

    inarytools.dodoc("ABOUT*", "AUTHORS", "COPYING", "NEWS", "README")
