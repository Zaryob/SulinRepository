#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "djvulibre-%s" % get.srcVERSION() if len(get.srcVERSION().split(".")) < 4 else "djvulibre-%s" % get.srcVERSION()[:get.srcVERSION().rfind(".")]

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--enable-threads \
                         --disable-desktopfiles \
                         --enable-xmltools \
                         --enable-i18n \
                         --with-jpeg \
                         --with-tiff")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.insinto("/usr/share/mime/packages", "desktopfiles/djvulibre-mime.xml")

    for size in ["22", "32", "48", "64"]:
        inarytools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" %(size, size), "desktopfiles/prebuilt-hi%s-djvu.png" % size, "image-vnd.djvu.png")

    inarytools.dodoc("COPY*", "README", "NEWS")
