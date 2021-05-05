#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
from inary.actionsapi import inarytools
from inary.actionsapi import autotools as tools
from inary.actionsapi import get
#more information : https://gitlab.com/sulinos/inary/tree/master/inary/actionsapi
def setup():
    tools.configure("--with-libpotrace")
def build():
    tools.make()

def install():
    tools.rawInstall("DESTDIR=%s" % get.installDIR())

