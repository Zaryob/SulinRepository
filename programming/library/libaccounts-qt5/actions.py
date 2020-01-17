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
    shelltools.system("sed -i 's|SUBDIRS  += Accounts tests|SUBDIRS += Accounts|' accounts-qt.pro")
    shelltools.system("qmake-qt5 PREFIX=/usr LIBDIR=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    inarytools.dodoc("NOTES", "INSTALL", "COPYING", "README.*", "TODO")
