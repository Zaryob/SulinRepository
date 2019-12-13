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
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    #shelltools.system("./autogen.sh --disable-gtk-doc --disable-docbook")

    options = '--with-package-name="GStreamer for Sulin" \
               --with-package-origin="http://www.github.com/SulinOS" \
               --disable-gtk-doc'

    if get.buildTYPE() == "emul32":
        options += " --bindir=/usr/bin32 \
                     --libdir=/usr/lib32 \
                     --libexecdir=/usr/libexec32 \
                     --disable-introspection"

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.configure(options)

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        inarytools.removeDir("/usr/bin32")
        inarytools.removeDir("/usr/libexec32")

    inarytools.removeDir("/usr/share/gtk-doc")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
