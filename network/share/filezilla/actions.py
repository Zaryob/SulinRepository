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
    #shelltools.export("WXRC", "/usr/bin/wxrc")
    #shelltools.export("LDFLAGS", "%s -lpthread" % get.LDFLAGS())
    #inarytools.dosed("data/filezilla.desktop", "Icon=filezilla", "Icon=/usr/share/pixmaps/filezilla.png")
    autotools.configure("--disable-static \
                         --disable-manualupdatecheck \
                         --disable-autoupdatecheck \
                         --with-pugixml=builtin \
                         --prefix=/usr ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move fzdefaults.xml.example to /usr/share/filezilla
    inarytools.domove("/usr/share/filezilla/docs/fzdefaults.xml.example", "/usr/share/filezilla")
    inarytools.removeDir("/usr/share/filezilla/docs")

    inarytools.dodoc("ChangeLog", "README", "AUTHORS")