#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get
import os

del(os.environ["JOBS"])

def setup():
    shelltools.system("./waf configure \
                        --prefix=/usr \
                        --libdir=/usr/lib \
                        --firewire \
                        --alsa ")

def build():
    shelltools.system("./waf build -v")

def install():
    shelltools.system("./waf --destdir=%s install" % get.installDIR())

    # be compatible with the former jackaudio
    inarytools.rename("/usr/bin/jack_rec", "jackrec")

    shelltools.chmod("%s/usr/lib/jack/*.so*" % get.installDIR(), 0o755)

    inarytools.dodoc("README*")
