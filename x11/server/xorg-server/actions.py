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
    autotools.autoreconf("-fi")

    autotools.configure("--enable-install-libxf86config \
                         --disable-systemd-logind \
                         --enable-aiglx \
                         --enable-glx-tls \
                         --enable-composite \
                         --enable-xcsecurity \
                         --enable-record \
                         --enable-dri \
                         --enable-dri2 \
                         --enable-glamor \
                         --enable-xwayland \
                         --enable-config-udev \
                         --disable-config-hal \
                         --enable-xfree86-utils \
                         --enable-xorg \
                         --enable-dmx \
                         --enable-xvfb \
                         --enable-xnest \
                         --enable-kdrive \
                         --enable-xfont \
                         --enable-kdrive-evdev \
                         --enable-kdrive-kbd \
                         --enable-kdrive-mouse \
                         --enable-xephyr \
                         --disable-xfake \
                         --disable-xfbdev \
                         --disable-devel-docs \
                         --disable-static \
                         --without-doxygen \
                         --with-pic \
                         --without-dtrace \
                         --with-int10=x86emu \
                         --with-os-name=\"Sulin\" \
                         --with-os-vendor=\"Sulin Community\" \
                         --with-builderstring=\"Package: %s\" \
                         --with-fontrootdir=/usr/share/fonts \
                         --with-default-font-path=catalogue:/etc/X11/fontpath.d,built-ins \
                         --with-xkb-output=/var/lib/xkb \
                         --with-dri-driver-path=/usr/lib/xorg/modules/dri \
                         --without-xmlto \
                         --without-fop \
                         --localstatedir=/var \
                         PCI_TXT_IDS_DIR=/usr/share/X11/pci \
                         " % get.srcTAG())

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

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
