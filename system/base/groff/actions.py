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
    autotools.autoreconf("-fi")
    shelltools.system("sed -i -e 's/^[ \t]\+g=g$/g=/' configure")
    shelltools.export("PAGE", "a4")
    autotools.configure("--prefix=/usr \
                         --without-x")

def build():
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    inarytools.dodir("/usr")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # required by man
    inarytools.dosym("eqn", "/usr/bin/geqn")
    inarytools.dosym("tbl", "/usr/bin/gtbl")
    inarytools.dosym("soelim", "usr/bin/zsoelim")
    inarytools.dodoc("ChangeLog", "NEWS", "PROBLEMS", "PROJECTS", "README")
