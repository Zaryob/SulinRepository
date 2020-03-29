#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import libtools

def build():
    shelltools.system("./configure -C \
		--sysconfdir=/etc \
		--datarootdir=/usr/share \
		--datadir=/usr/share \
		--mandir=/usr/share/man\
		--prefix=/usr \
		--enable-build-in-source-tree")
    autotools.make()
 
def install():
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())
    shelltools.system('sed -i "s/\/x86_64-pc-linux-gnu//g" {}/usr/lib/x86_64-pc-linux-gnu/pkgconfig/*'.format(get.installDIR()))
    shelltools.system("mv {0}/usr/texmf-dist/ {0}/usr/share/texmf-dist".format(get.installDIR()))
    shelltools.system("cp -prf {0}/usr/lib/x86_64-pc-linux-gnu/* {0}/usr/lib/".format(get.installDIR()))
    shelltools.system("rm -rf {0}/usr/lib/x86_64-pc-linux-gnu/".format(get.installDIR()))
