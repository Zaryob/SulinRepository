#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import scons
from inary.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def build():
    scons.make('PREFIX=/usr \
                COMPILE_FLAGS="%s %s -lpthread" \
                BUILD_TESTS=0 \
                PYTHON=/usr/bin/python3' % (get.CXXFLAGS(), get.LDFLAGS()))

def install():
    scons.install("install WILL_DEAL_WITH_XDG_MYSELF=1 DESTDIR=%s" % get.installDIR())

    inarytools.dodir("/usr/share/applications")
    inarytools.dosym("/usr/share/libffado/icons/hi64-apps-ffado.png", "/usr/share/pixmaps/ffado-mixer.png")

    inarytools.domove("/usr/man/", "/usr/share")

    inarytools.dodoc("AUTHORS", "ChangeLog", "LICENSE*", "TODO", "README")
