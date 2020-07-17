#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("LDFLAGS",get.LDFLAGS()+" -lm -lasound")
    mesontools.meson_configure("-D package-name=\"GStreamer Bad Plugins (Sulin)\" \
                                -D package-origin=\"https://www.gitlab.com/sulinos\"")

def build():
    shelltools.export("LDFLAGS",get.LDFLAGS()+" -lm -lasound")
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

    inarytools.dodoc( "AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "RELEASE", "REQUIREMENTS")
