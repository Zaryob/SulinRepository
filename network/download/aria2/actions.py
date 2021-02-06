# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--enable-bittorrent \
                         --enable-libaria2 \
                         --enable-metalink \
                         --enable-epoll \
                         --enable-nls \
                         --disable-rpath \
                         --with-gnutls \
                         --with-openssl \
                         --with-sqlite3 \
                         --with-libxml2 \
                         --with-libcares \
                         --with-libz \
           --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt")

def build():
    autotools.make("-C po update-gmo")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("ABOUT*", "AUTHORS", "ChangeLog", "COPYING", "LICENSE*", "NEWS", "README*")
