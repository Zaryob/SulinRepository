#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import mesontools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure("-Dminer_rss=false -Dsystemd_user_services=false -Ddocbook=false -Dman=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    shelltools.system("sed -i 's/OnlyShowIn=.*/OnlyShowIn=GNOME;/g' {}/etc/xdg/autostart/tracker-miner-fs-3.desktop".format(get.installDIR()))
    shelltools.system("echo Hidden=true >> {}/etc/xdg/autostart/tracker-miner-fs-3.desktop".format(get.installDIR()))
