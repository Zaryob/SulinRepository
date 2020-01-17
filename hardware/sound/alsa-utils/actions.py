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
    autotools.configure("--disable-maintainer-mode \
                         --with-asound-state-dir=/var/lib/alsa \
                         --with-udev-rules-dir=/lib/udev/rules.d \
                         --sbindir=/sbin \
                         --disable-alsaconf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    inarytools.dodoc("ChangeLog", "seq/aconnect/README.aconnect", "seq/aseqnet/README.aseqnet")
