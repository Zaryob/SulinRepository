# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure("-D os_vendor=\"Sulin OS\" \
                                -D ipv6=true \
                                -D dmx=true \
                                -D xvfb=true \
                                -D xnest=true \
                                -D xcsecurity=true \
                                -D xorg=true \
                                -D xephyr=true \
                                -D xwayland=true \
                                -D xwayland_eglstream=true \
                                -D glamor=true \
                                -D udev=true \
                                -D systemd_logind=true \
                                -D suid_wrapper=true \
                                -D xkb_dir=/usr/share/X11/xkb \
                                -D xkb_output_dir=/var/lib/xkb ")

def build():
    mesontools.ninja_build()

def install():

    mesontools.ninja_install()
    inarytools.domove("/usr/share/pkgconfig", "/usr/lib")
    inarytools.dodoc("COPYING", "README.md")
