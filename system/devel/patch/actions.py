# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--prefix=/usr")

def build():
    #autotools.make('LDFLAGS="%s"' % get.LDFLAGS())
    autotools.make()
    
def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
