#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("LC_ALL", "C")

def setup():

    autotools.rawConfigure('\
		--prefix=/usr \
		--sysconfdir=/etc \
		--localstatedir=/var \
		--libexecdir=/usr/lib/qemu \
		--smbd=/usr/bin/smbd \
		--enable-modules \
		--enable-sdl \
		--audio-drv-list="pa alsa sdl"')

def build():

    autotools.make("-j1") # -j5 not good

def install():
    autotools.rawInstall('DESTDIR="{}"'.format(get.installDIR()))


