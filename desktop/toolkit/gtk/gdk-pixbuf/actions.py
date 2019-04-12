#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    options = "\
                 --disable-static \
                 --disable-silent-rules \
                 --with-libjasper \
                 --with-x11 \
                 --with-included-loaders=png \
              "

    options += "\
                 --bindir=/_emul32/bin \
                 --disable-introspection \
               " if get.buildTYPE() == "emul32" else \
               "\
                 --enable-introspection \
               "
    autotools.configure(options)

    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        inarytools.domove("/_emul32/bin/gdk-pixbuf-query-loaders", "/usr/bin", "gdk-pixbuf-query-loaders-32")
        inarytools.removeDir("/_emul32")
        return
    inarytools.dosym("/usr/bin/gdk-pixbuf-query-loaders", "/usr/bin/gdk-pixbuf-query-loaders-64")
    inarytools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
