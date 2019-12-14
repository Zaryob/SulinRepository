#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    inarytools.dosed("avahi-daemon/avahi-daemon.conf", "^#(disallow-other-stacks=)no", "\\1yes")

    # fix avahi socket path
    inarytools.dosed('configure.ac', '^(avahi_runtime_dir=")\$\{localstatedir\}(\/run")', r'\1\2')

    autotools.autoreconf("-fi")
    # --with-systemdsystemunitdir=/lib/systemd/system
    autotools.configure("\
                         --with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-qt3 \
                         --disable-qt4 \
                         --disable-doxygen-doc \
                         --enable-glib \
                         --enable-gobject \
                         --enable-introspection \
                         --disable-mono \
                         --disable-python \
                         --enable-gtk3 \
                         --enable-compat-howl \
                         --enable-compat-libdns_sd \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi-autoipd \
                         --with-autoipd-group=avahi-autoipd \
                         --with-avahi-priv-access-group=avahi \
                         --with-dbus-system-address=unix:path=/run/dbus/system_bus_socket \
                        ")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Add missing symlinks for avahi-compat-howl and avahi-compat-dns-sd
    inarytools.dosym("/usr/lib/pkgconfig/avahi-compat-howl.pc", "/usr/lib/pkgconfig/howl.pc")
    inarytools.dosym("/usr/lib/pkgconfig/avahi-compat-libdns_sd.pc", "/usr/lib/pkgconfig/libdns_sd.pc")
    inarytools.dosym("/usr/include/avahi-compat-libdns_sd/dns_sd.h", "/usr/include/dns_sd.h")

    # Remove example
    inarytools.remove("/etc/avahi/services/sftp-ssh.service")

    inarytools.dodir("/run/avahi-daemon")
    inarytools.dodir("/var/lib/avahi-autoipd")

    inarytools.dodoc("docs/AUTHORS", "docs/README", "docs/TODO")
    inarytools.removeDir("/usr/lib/avahi")
