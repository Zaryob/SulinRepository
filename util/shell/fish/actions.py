#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WORKDIR="fish-shell-3.0.2"

def setup():
    shelltools.system("autoreconf -fiv")
    autotools.configure("docdir=/%s/%s" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

