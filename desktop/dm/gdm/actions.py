#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    shelltools.export("SYSTEMD_LIBS","-lelogind")
    shelltools.export("SYSTEMD_CFLAGS","-I/usr/include/elogind")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--without-plymouth    \
            --disable-static      \
            --enable-gdm-xsession \
            --with-pam-mod-dir=/lib/security\
            --without-xevie\
            --without-plymouth \
            --without-tcp-wrappers\
            --enable-authentication-scheme=pam\
            --with-systemdsystemunitdir=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

