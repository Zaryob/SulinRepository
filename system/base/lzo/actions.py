#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--enable-shared")

    shelltools.chmod("examples/*", 0o644)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "doc/LZO*")

    inarytools.insinto(examples, "examples/*.c")
    inarytools.insinto(examples, "examples/*.h")
