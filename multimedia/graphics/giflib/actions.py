#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def build():
    autotools.make()

def install():
    autotools.install("DESTDIR={}".format(get.installDIR()))
    inarytools.dohtml("doc/")
    inarytools.domove("/usr/local/share/*","/usr/share/")
    inarytools.domove("/usr/local/*","/usr")
    inarytools.removeDir("/usr/local/")
    inarytools.removeDir("/usr/share/share")
