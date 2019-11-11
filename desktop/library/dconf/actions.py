#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltools.system("sed -i 's|link_whole|link_with|' common/meson.build && \
sed -i 's/module/& | grep -v mangle_path/' gsettings/abicheck.sh")
    mesontools.meson_configure()

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
