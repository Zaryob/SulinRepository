#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools

def setup():
    mesontools.meson_configure()

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

    inarytools.removeDir("/dev")
 #   inarytools.removeDir("/etc")

    # Make compat symlinks into /usr/bin
    inarytools.dosym("/bin/fusermount", "/usr/bin/fusermount")
    inarytools.dosym("/bin/ulockmgr_server", "/usr/bin/ulockmgr_server")


