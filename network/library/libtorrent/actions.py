#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "libtorrent-libtorrent-1_2_3"


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_STANDARD=11")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.domove("/usr/usr/lib","/usr/lib")
    inarytools.removeDir("/usr/usr")

    inarytools.dohtml("docs/*")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
