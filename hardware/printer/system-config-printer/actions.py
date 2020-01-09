#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    # we are using different paths
    inarytools.dosed("cupshelpers/cupshelpers.py", "\/lib64\/", "\/lib\/")
    inarytools.dosed("troubleshoot/CheckUSBPermissions.py", "\/usr\/bin\/getfacl", "\/bin\/getfacl")

    inarytools.dosed("Makefile.in", "xmlto man", "xmlto --skip-validation man")
    autotools.configure("--with-udev-rules \
                         --with-systemdsystemunitdir=no \
                         --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s udevrulesdir=/lib/udev/rules.d udevhelperdir=/lib/udev" % get.installDIR())

    inarytools.dodir("/run/udev-configure-printer")

