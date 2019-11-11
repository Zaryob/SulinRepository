#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr --sysconfdir=/etc \
                         --with-ssl=openssl")

def build():
    autotools.make()

def install():
    autotools.install()

    # default root certs location
    shelltools.echo("%s/etc/wgetrc" % get.installDIR(), "ca_certificate=/etc/ssl/certs/ca-certificates.crt")

    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "NEWS", "README", "MAILING-LIST")
