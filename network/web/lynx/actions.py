#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-warnings \
                         --enable-8bit-toupper \
                         --enable-externs \
                         --enable-cgi-links \
                         --enable-persistent-cookies \
                         --enable-prettysrc \
                         --enable-source-cache \
                         --enable-charset-choice \
                         --enable-default-colors \
                         --enable-nested-tables \
                         --enable-read-eta \
                         --with-zlib \
                         --enable-nls \
                         --enable-ipv6 \
                         --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS*", "AUTHORS", "CHANGES", "COPYING", "INSTALLATION","README")

    inarytools.dobin("lynx")
