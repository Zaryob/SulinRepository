#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    autotools.configure("--enable-all-themes   \
                         --enable-test-themes  \
                         --enable-icon-mapping \
                        --with-gtk3 \
                         --enable-test-themes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #fix conflict with gnome-themes
    shelltools.system("rm -rf {}/usr/share/themes/HighContrastInverse".format(get.installDIR()))
    inarytools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS")
