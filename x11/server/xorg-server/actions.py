# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
#    shelltools.chmod("hw/vnc/symlink-vnc.sh")
#    autotools.autoreconf("-fi")
    #shelltools.export("CFLAGS","{} D_GNU_SOURCE -D__gid_t=gid_t -D__uid_t=uid_t".format(get.CFLAGS()))
    shelltools.export("LDFLAGS","{} -Wl,-z,lazy".format(get.LDFLAGS()))
    autotools.configure('--sysconfdir=/etc/X11 \
		--localstatedir=/var \
		--with-xkb-path=/usr/share/X11/xkb \
		--with-xkb-output=/var/lib/xkb \
		--without-systemd-daemon \
		--enable-composite \
		--enable-config-udev \
		--enable-dri \
		--enable-dri2 \
		--enable-dri3 \
		--enable-glamor \
		--enable-ipv6 \
		--enable-kdrive \
		--enable-xace \
		--enable-xcsecurity \
		--enable-xephyr \
		--enable-xnest \
		--enable-xorg \
		--enable-xres \
		--enable-xv \
		--enable-xwayland \
		--disable-config-hal \
		--disable-dmx \
		--disable-systemd-logind \
		--with-os-vendor="sulin"')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodir("/etc/X11/fontpath.d")
    inarytools.dodir("/etc/X11/xorg.conf.d")
    inarytools.dodir("/usr/share/X11/pci")
    inarytools.dodir("/usr/share/X11/xorg.conf.d")

    # Remove empty dir
    inarytools.removeDir("/var/log")

    inarytools.dodoc("COPYING", "README.md")

