#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def build():
    for directory in ["freeglut","freetype","harfbuzz","jbig2dec","libjpeg","openjpeg","zlib"]:
        shelltools.unlinkDir("thirdparty/"+directory)

    shelltools.export("USE_SYSTEM_LIBS",'yes')
    shelltools.system("sed '/TOFU_CJK /c #define TOFU_CJK 1/' -i include/mupdf/fitz/config.h")
    shelltools.system("sed -i '/ttc/s/^/#/' Makefile")
    autotools.make("prefix=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())

    inarytools.dodoc("CHANGES", "README", "COPYING")
