#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
     autotools.configure("--disable-fd-passing \
                          --disable-static \
                          --disable-gpgsm-test \
                          --enable-languages=cpp,python,qt")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
