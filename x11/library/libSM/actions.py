# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
import os

if get.buildTYPE() == "emul32":
        shelltools.export("CC","gcc -m32")
        shelltools.export("CXX","g++ -m32")
        shelltools.export("LDFLAGS","-m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")

os.system("export")
def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --without-xmlto \
                         --with-libuuid \
                         --without-fop")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
