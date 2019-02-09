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
    #who knows inarytools.dosed :)
    cmd="sed -i '/gets is a security hole/d' gnu/stdio.in.h"
    shelltools.system(cmd)
    autotools.configure("--enable-nls \
                         --bindir=/bin \
                         --with-rmt=/usr/sbin/rmt \
                         --disable-rpath")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/usr/share/man/man8")
    #inarytools.removeDir("/usr/libexec")

    inarytools.dodoc("ChangeLog", "NEWS", "README")

