# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure('-Ddmx=true \
		-Ddri2=true \
		-Ddri3=true \
		-Dglamor=true \
		-Dglx=true \
		-Dhal=false \
		-Dipv6=true \
		-Dlinux_acpi=true \
		-Dos_vendor="Sulin" \
		-Dsuid_wrapper=true \
		-Dsystemd_logind=true \
		-Dudev=true \
		-Dxcsecurity=true \
		-Dxephyr=true \
		-Dxkb_dir=/usr/share/X11/xkb \
		-Dxkb_output_dir=/var/lib/xkb \
		-Dxnest=true \
		-Dxorg=true \
		-Dxvfb=true \
		-Dxwayland=true \
		-Dxwayland_eglstream=true')

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    inarytools.dosym("Xorg","/usr/bin/X")
    
