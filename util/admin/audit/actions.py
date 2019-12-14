#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --with-libcap-ng=yes \
                         --enable-gssapi-krb5=no \
                         --enable-systemd=no \
                         --with-python=yes \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("-j1 check")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # remove RH specific bits
    inarytools.removeDir("/etc/sysconfig")
    inarytools.removeDir("/etc/rc.d")

    # Create data directories
    inarytools.dodir("/var/log/audit")
    inarytools.dodir("/var/spool/audit")

    # Disable zos-remote plugin to get rid of deps. like cyrus-sasl
    inarytools.remove("/usr/share/man/man8/audispd-zos-remote.8")
    inarytools.remove("/usr/share/man/man5/zos-remote.conf.5")

