#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure("-Dcgroup-controller=elogind \
		-Dhalt-path=/sbin/halt \
		-Drootlibexecdir=/usr/libexec/elogind \
		-Dreboot-path=/sbin/reboot \
		-Ddefault-hierarchy=hybrid \
		-Ddefault-kill-user-processes=false \
		-Dpolkit=true \
		-Ddebug=true --buildtype=debug \
		-Dman=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    if get.buildTYPE()=="emul32":
        inarytools.unlinkDir("{}/usr/pkgconfig".format(get.installDIR()))
        return
    inarytools.dodoc("README*", "LICENSE.GPL2", "LICENSE.LGPL2.1")
