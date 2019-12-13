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
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr --enable-gtk3 --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

    shelltools.chmod("{}/etc/lxdm/lxdm.conf".format(get.installDIR()), 0o644)
    inarytools.dodir("/usr/lib/sysusers.d")
    inarytools.dodir("/usr/lib/tmpfiles.d")
    # Setup system user and group
    shelltools.echo("{}/usr/lib/sysusers.d/lxdm.conf".format(get.installDIR()),
                    'u lxdm - "Lightweight X11 Display Manager" /var/lib/lxdm'
                    )
    shelltools.echo("{}/usr/lib/tmpfiles.d/lxdm.conf".format(get.installDIR()),
                    'd /var/lib/lxdm 0700 lxdm lxdm - -')

    inarytools.dodoc("COPYING", "AUTHORS", "TODO", "README", "ChangeLog", "NEWS")
