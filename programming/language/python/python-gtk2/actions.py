#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "pygtk-%s" % (get.srcVERSION())

def setup():
    shelltools.unlink("py-compile" )
    shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())

    autotools.configure("PYTHON=/usr/bin/python2 \
                         --prefix=/usr \
                         --enable-thread \
                         --enable-numpy")

    shelltools.touch("%s/style.css" % get.curDIR())
    inarytools.dosed("docs/Makefile", "CSS_FILES = .*", "CSS_FILES = %s/style.css" % get.curDIR())

    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "MAPPING", "NEWS", "README", "THREADS", "TODO")
