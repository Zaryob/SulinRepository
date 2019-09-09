# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    inarytools.dosed("Makefile", "MANDIR = /usr/man", "MANDIR = /usr/share/man")
    autotools.make("-C po update-po")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/sbin")
    inarytools.removeDir("/usr/lib/")
    inarytools.dodoc("COPYING")
