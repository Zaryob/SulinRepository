#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure("-Dpatched-ubuntu-autostarts=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    shelltools.system('sed -i "s|/usr/lib/gnome-settings-daemon/|/usr/libexec/|g" {}/etc/xdg/autostart/*'.format(get.installDIR()))
