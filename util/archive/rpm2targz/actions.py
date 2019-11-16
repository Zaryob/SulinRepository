#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="rpm2targz-%s" % get.srcVERSION()


def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    inarytools.dodoc("*.README*")
