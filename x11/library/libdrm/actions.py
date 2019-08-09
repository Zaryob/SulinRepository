# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    #inarytools.dosed("configure.ac", "pthread-stubs", deleteLine=True)
    mesontools.meson_configure(" -Dudev=false \
    -Dvalgrind=false")
def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
