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
    if get.buildTYPE() == "emul32":
        inarytools.dosed("configure.ac", "(.*OC_X86_64_ASM.*)", r"#\1")
        shelltools.system("./autogen.sh")
    autotools.configure("--enable-shared \
                         --enable-encode \
                         --disable-dependency-tracking \
                         --disable-spec \
                         --disable-sdltest \
                         --disable-examples \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" docdir=/%s/libtheora' % (get.installDIR(), get.docDIR()))

    inarytools.dodoc("README", "AUTHORS", "CHANGES")
