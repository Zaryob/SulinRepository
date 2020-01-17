#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --builtin-libraries=replace \
                         --bundled-libraries=NONE \
                         --disable-rpath \
                        ")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("docs/README")
