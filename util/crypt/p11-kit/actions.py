#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools

def setup():
    mesontools.meson_configure(" --buildtype debugoptimized \
    -D gtk_doc=false \
    -D man=false \
    -D trust_paths=/etc/ca-certificates/trust-source:/usr/share/ca-certificates/trust-source")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

    if get.buildTYPE() == "emul32":
        inarytools.domove("/usr/pkgconfig", "/usr/lib32/")
        inarytools.domove("/usr/p11-kit-proxy.so", "/usr/lib32")
        inarytools.domove("/usr/pkcs11", "/usr/lib32/")
        inarytools.domove("/usr/*.so*", "/usr/lib32/")
        return

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
