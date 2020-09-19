#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import mesontools
from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="mutter-3.36.1"

def setup():
    mesontools.meson_configure("-Degl_device=true \
		-Dudev=true \
		-Dnative_backend=true \
		-Dintrospection=true \
		-Dxwayland_path=/usr/bin/Xwayland \
		-Dremote_desktop=true \
		-Dprofiler=false ")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    inarytools.remove("/usr/bin/mutter")
    inarytools.removeDir("/usr/share/locale")
    inarytools.removeDir("/usr/share/glib-2.0")
    inarytools.removeDir("/usr/share/GConf")
    inarytools.removeDir("/usr/share/man")
    inarytools.removeDir("/usr/share/applications")
    inarytools.removeDir("/usr/share/gnome-control-center")
    
