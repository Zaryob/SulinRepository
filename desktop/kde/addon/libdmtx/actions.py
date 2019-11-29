# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("CC", "{} -std=c99".format(get.CC()))
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    shelltools.export("CC", "{} -std=c99".format(get.CC()))
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "NEWS", "README", "README.linux")
