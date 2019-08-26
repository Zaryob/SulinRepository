#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.rename("/usr/share/doc/sgml-common-%s" % get.srcVERSION(), get.srcNAME())
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
