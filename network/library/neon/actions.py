#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--with-libxml2 \
                         --with-expat \
                         --without-gssapi \
                         --without-libproxy \
                         --with-ssl=openssl \
                         --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt \
                         --enable-threadsafe-ssl=posix \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("THANKS", "TODO", "ChangeLog", "AUTHORS", "BUGS", "NEWS", "README", "doc/*.txt")
