#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-xrandr \
                         --enable-xcursor \
                         --enable-libnotify \
                         --enable-libxklavier \
                         --enable-xorg-libinput \
                         --enable-colord \
                         --enable-pluggable-dialogs \
                         --enable-sound-settings")

def build():
    autotools.make()

def install():
    autotools.install()
    # fix conflict with exo
    inarytools.removeDir("/usr/share/xfce4/helpers/")
    inarytools.remove("/etc/xdg/xfce4/helpers.rc")
    inarytools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
