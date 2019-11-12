#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-nasm \
                         --enable-shared \
                         --enable-mp3rtp \
                         --disable-static \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" pkghtmldir="/%s/%s/html"' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    inarytools.dodoc("API", "ChangeLog", "HACKING", "README*", "STYLEGUIDE", "TODO", "USAGE")
    inarytools.dohtml("misc/*", "Dll/*")
    inarytools.dobin("misc/mlame")

    inarytools.remove("/usr/lib/libmp3lame.so")
    inarytools.remove("/usr/lib/libmp3lame.so.0")



    inarytools.dosym("/usr/lib/libmp3lame.so.0.0.0", "/usr/lib/libmp3lame.so")
    inarytools.dosym("/usr/lib/libmp3lame.so.0.0.0", "/usr/lib/libmp3lame.so.0")