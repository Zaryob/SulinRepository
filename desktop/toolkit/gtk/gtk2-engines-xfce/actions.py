#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltools.system("sed -i 's/\xd6/\xc3\x96/' gtk-3.0/xfce_style_types.h")
    autotools.configure("--prefix=/usr --enable-gtk3")


def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS")
