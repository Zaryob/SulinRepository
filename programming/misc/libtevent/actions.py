#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

jobs = get.makeJOBS().replace("-j", "")

def setup():
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --builtin-libraries=replace \
                         --bundled-libraries=NONE \
                         --disable-rpath \
                        ")

def build():
    autotools.make("JOBS=%s" % jobs)

def install():
    autotools.rawInstall("DESTDIR=%s JOBS=%s" % (get.installDIR(), jobs))

#    inarytools.remove("/usr/lib/*.a")

    # Create symlinks for so file
#    inarytools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so.%s" % get.srcVERSION().split(".")[0])
#    inarytools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so")
