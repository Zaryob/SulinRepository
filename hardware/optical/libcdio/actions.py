#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --with-cd-paranoia-name=libcdio-paranoia \
                         --disable-vcd-info \
                         --enable-cpp-progs \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % (get.installDIR()))

    inarytools.dosed("%s/usr/include/cdio/version.h" % get.installDIR(), '%s[^"]+' % get.srcVERSION(), get.srcVERSION())
    inarytools.dosed("%s/usr/include/cdio/cdio_config.h" % get.installDIR(), "#define\s(CDIO_LIBCDIO_SOURCE_PATH).*", r"#undef \1")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
