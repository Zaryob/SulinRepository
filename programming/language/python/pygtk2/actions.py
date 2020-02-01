#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
import os

def setup():
    shelltools.system("sed -i -e 's#env python$#env python2#' examples/pygtk-demo/{,demos/}*.py")
    shelltools.export("PYTHON","/usr/bin/python2")
    autotools.configure("--prefix=/usr")
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    _env=os.environ.copy()
    os.environ.clear()
    os.system("make")
    os.environ.update(_env)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "MAPPING", "NEWS", "README", "THREADS", "TODO")
