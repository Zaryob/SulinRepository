# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    shelltools.system("./autogen.sh")

    autotools.configure("--libdir=/usr/lib --with-tests")

def build():
    autotools.make()

def check():
    shelltools.cd("tests")
    shelltools.system("./test_all.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING", "NEWS", "README")