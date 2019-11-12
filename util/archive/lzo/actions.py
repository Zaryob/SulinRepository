#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--enable-shared \
                         --disable-dependency-tracking")

    shelltools.chmod("examples/*", 0o644)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "doc/LZO*")

    inarytools.insinto(examples, "examples/*.c")
    inarytools.insinto(examples, "examples/*.h")
