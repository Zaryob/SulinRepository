#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    mesontools.meson_configure("-Ddocbook=false -Dgtk_doc=false")
    
def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install("DESTDIR=%s" % get.installDIR())

