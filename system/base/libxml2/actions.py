#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    # fix sandbox violations when attempt to read "/missing.xml"
    inarytools.dosed("testapi.c", "\/missing.xml", "missing.xml")

    options = "--with-zlib \
               --with-readline \
               --enable-ipv6 \
               --disable-static \
               --with-threads \
               --with-history \
              "

    if get.buildTYPE() == "emul32":
        options += " --bindir=/emul32/bin \
                     --without-python"
    else: options += " --with-python={}".format(
    "/usr/bin/python2" if get.buildTYPE()=="rebuild_python" else "/usr/bin/python3")

    autotools.configure(options)
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    if get.buildTYPE()=="rebuild_python":
        autotools.rawInstall("DESTDIR='%s/python2'" % get.installDIR())
        shelltools.move("%s/python2/usr/lib/python2.7" % get.installDIR(),
                        "%s/usr/lib/python2.7" % get.installDIR())
        shelltools.unlinkDir("%s/python2" % get.installDIR())
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32" or "i686":
        inarytools.removeDir("/usr/share/gtk-doc")
        return

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
